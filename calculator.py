"""
calculator.py
-------------
Contains the core logic for calculating utility splits.
"""

from typing import List, Dict, Any
from models import Resident
from utils import get_float_input, get_int_input

class UtilityCalculator:
    """
    Controller class for managing residents, costs, and performing calculations.
    """
    def __init__(self):
        self.residents: List[Resident] = []
        self.costs: Dict[str, float] = {
            'water': 0.0,
            'waste': 0.0,
            'storm': 0.0,
            'transport': 0.0,
            'electric_total': 0.0
        }
        self.ev_usage: List[Dict[str, Any]] = [] 

    def interactive_setup_residents(self):
        """Manually configure residents via CLI."""
        from utils import get_bool_input
        print("\n--- Resident Setup ---")
        count = get_int_input("How many residents in the household? ")
        
        # Step 1: Collect all names
        for i in range(count):
            name = input(f"Resident {i}: Enter name: ")
            self.residents.append(Resident(name, split_weight=1.0))
            
        # Step 2: Ask for couples by index
        has_couples = get_bool_input("\nAre there any couples? (y/n): ")
        if has_couples:
            print("\nPlease select residents who are part of a couple (enter index numbers separated by a comma, e.g. '0, 1'):")
            for idx, res in enumerate(self.residents):
                print(f"  {idx}: {res.name}")
            
            valid_indices = False
            while not valid_indices:
                selection = input("Indices: ")
                try:
                    parts = selection.split(',')
                    user_indices = [int(p.strip()) for p in parts]
                    if all(0 <= u < len(self.residents) for u in user_indices):
                        valid_indices = True
                        for idx in user_indices:
                            self.residents[idx].is_couple = True
                    else:
                        print("Invalid indices selected.")
                except ValueError:
                    print("Invalid format. Use comma separated numbers like '0, 1'")
                    
        print(f"\n--- Configured {len(self.residents)} billing entities ---")

    def interactive_input_costs(self):
        """Manually input bill totals."""
        print("\n--- Enter Monthly Bill Totals ---")
        self.costs['electric_total'] = get_float_input("Electric Meter: $")
        self.costs['transport'] = get_float_input("Transportation: $")
        self.costs['water'] = get_float_input("Water Meter: $")
        waste_water = get_float_input("Waste Water: $")
        self.costs['storm'] = get_float_input("Storm Water: $")
        solid_waste = get_float_input("Solid Waste: $")
        
        # Combine waste for calculation logic 
        self.costs['waste'] = waste_water + solid_waste

    def interactive_input_ev(self):
        """Manually input EV details."""
        from utils import get_bool_input
        print("\n--- Electric Vehicle Setup ---")
        
        has_ev = get_bool_input("Is there any EV charging to account for? (y/n): ")
        if not has_ev:
            return

        num_ev_groups = get_int_input("How many separate EV charging groups? ")
        
        for i in range(num_ev_groups):
            print(f"\nConfiguring EV Group {i+1}")
            print("Select residents who share this EV (enter index numbers separated by comma):")
            for idx, res in enumerate(self.residents):
                print(f"  {idx}: {res.name}")
            
            valid_indices = False
            user_indices = []
            while not valid_indices:
                selection = input("Indices: ")
                try:
                    parts = selection.split(',')
                    user_indices = [int(p.strip()) for p in parts]
                    if all(0 <= u < len(self.residents) for u in user_indices):
                        valid_indices = True
                    else:
                        print("Invalid indices selected.")
                except ValueError:
                    print("Invalid format. Use comma separated numbers like '0, 2'")

            kwh = get_float_input("Enter kWh used by this group: ")
            rate = get_float_input("Enter rate per kWh for this group (e.g. 0.15): ")
            
            self.ev_usage.append({
                'users': user_indices,
                'kwh': kwh,
                'rate': rate
            })

    def calculate(self):
        """Performs the cost splitting logic."""
        if not self.residents:
            return

        # Total Weight
        total_weight = sum(r.split_weight for r in self.residents)
        print(f"\nTotal Billing Weights: {total_weight}")

        # 1. Base Utilities Split
        base_total = (self.costs['water'] + 
                      self.costs['waste'] + 
                      self.costs['storm'] + 
                      self.costs['transport'])
        
        cost_per_weight = base_total / total_weight
        
        for res in self.residents:
            res.base_utilities_share = cost_per_weight * res.split_weight

        # 2. Electric Bill Split
        # Calculate total cost attributed to EVs
        total_ev_cost = 0.0
        
        for usage in self.ev_usage:
            cost = usage['kwh'] * usage['rate']
            total_ev_cost += cost
            
            # Split this specific EV cost among its users
            users_in_group = usage['users']
            split_cost = cost / len(users_in_group)
            
            for u_idx in users_in_group:
                # Find the resident object by index (assuming order matches setup)
                # Note: ev_usage stores indices into self.residents
                self.residents[u_idx].ev_charge_cost += split_cost

        # Remaining electric cost
        common_electric = self.costs['electric_total'] - total_ev_cost
        
        if common_electric < 0:
            print(f"\nWARNING: Calculated EV costs (${total_ev_cost:.2f}) exceed Total Electric Bill (${self.costs['electric_total']:.2f}).")
            common_electric = 0 

        electric_per_weight = common_electric / total_weight
        for res in self.residents:
            res.common_electric_share = electric_per_weight * res.split_weight

    def print_report(self):
        """Prints the final breakdown."""
        print("\n" + "="*40)
        print(" FINAL BILL REPORT ")
        print("="*40)
        
        grand_total = 0.0
        
        # Combine couples regardless of the order they were entered
        combined_residents = []
        processed_couples = set()
        
        for i in range(len(self.residents)):
            res = self.residents[i]
            
            # If we've already merged this resident as part of a couple, skip them
            if id(res) in processed_couples:
                continue
                
            if res.is_couple:
                # Find the next available partner
                partner = None
                for j in range(i + 1, len(self.residents)):
                    if self.residents[j].is_couple and id(self.residents[j]) not in processed_couples:
                        partner = self.residents[j]
                        break
                        
                if partner:
                    # Create a temporary Resident to represent the combined couple
                    combined = Resident(
                        name=f"{res.name} & {partner.name}",
                        split_weight=2.0
                    )
                    
                    combined.base_utilities_share = res.base_utilities_share + partner.base_utilities_share
                    combined.common_electric_share = res.common_electric_share + partner.common_electric_share
                    combined.ev_charge_cost = res.ev_charge_cost + partner.ev_charge_cost
                    
                    combined_residents.append(combined)
                    processed_couples.add(id(res))
                    processed_couples.add(id(partner))
                else:
                    # Rare edge case: odd number of people marked as is_couple
                    combined_residents.append(res)
            else:
                combined_residents.append(res)
                
        for res in combined_residents:
            print(res)
            print("-" * 20)
            grand_total += res.total_due()
            
        print(f"Total Collected: ${grand_total:.2f}")
        
        actual_total = (self.costs['water'] + self.costs['waste'] + 
                        self.costs['storm'] + self.costs['transport'] + 
                        self.costs['electric_total'])
                        
        print(f"Actual Bill Total: ${actual_total:.2f}")
        diff = grand_total - actual_total
        if abs(diff) > 0.01:
            print(f"Discrepancy: ${diff:.2f}")
        else:
            print("Balance Check: OK")
