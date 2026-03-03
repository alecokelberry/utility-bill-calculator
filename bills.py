"""
bills.py
--------
Stores archived bill data and configuration/setup logic.
This allows for easy reproduction of past bills.
"""

from typing import List, Dict, Any
from models import Resident

def load_dec_2025_jan_2026_data() -> Dict[str, Any]:
    """
    Returns the configuration data for the Dec 11, 2025 - Jan 12, 2026 bill period.
    
    Returns:
        dict: containing 'residents', 'costs', and 'ev_usage' keys.
    """
    print("\n--- Loading Data for Bill Period: Dec 11, 2025 - Jan 12, 2026 ---")
    
    # 1. Setup Residents
    residents = [
        Resident("Resident 1 & 2 (Couple)", split_weight=2.0),
        Resident("Resident 3", split_weight=1.0),
        Resident("Resident 4", split_weight=1.0)
    ]
    
    # 2. Setup Costs
    # Waste = Waste Meter (81.82) + Solid Waste (22.84)
    costs = {
        'water': 43.18,
        'waste': 81.82 + 22.84,
        'storm': 11.40,
        'transport': 2.52,
        'electric_total': 145.99
    }
    
    # 3. Setup EV Usage
    # Resident 1 & 2: 544 kWh @ $0.045
    # Resident 4: 276.1 kWh @ $0.07
    ev_usage = [
        {
            'users': [0], # Index 0 is the couple
            'kwh': 544.0,
            'rate': 0.045
        },
        {
            'users': [2], # Index 2 is Resident 4
            'kwh': 276.1,
            'rate': 0.07
        }
    ]
    
    return {
        'residents': residents,
        'costs': costs,
        'ev_usage': ev_usage
    }

def load_manual_setup_data() -> Dict[str, Any]:
    """
    Returns the basic structure for a manual setup.
    Use this if you want to prompt the user (logic handled in Calculator/Main).
    For now, this just helps pre-seed the residents if needed.
    """
    # This function is a placeholder if we want to move manual input logic here.
    pass
