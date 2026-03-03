"""
models.py
---------
Defines the data structures for the Utility Bill Calculator.
"""

class Resident:
    """
    Represents a resident or billing entity.
    
    Attributes:
        name (str): The display name of the resident.
        split_weight (float): The weighting for shared costs (default 1.0).
                              e.g. A couple might have a weight of 2.0.
        base_utilities_share (float): Calculated share of base utilities (Water, Waste, etc).
        common_electric_share (float): Calculated share of common electric costs.
        ev_charge_cost (float): Specific cost assigned for EV charging.
    """
    def __init__(self, name: str, split_weight: float = 1.0):
        self.name = name
        self.split_weight = split_weight
        self.base_utilities_share = 0.0
        self.common_electric_share = 0.0
        self.ev_charge_cost = 0.0

    def total_due(self) -> float:
        """Returns the total cost associated with this resident."""
        return self.base_utilities_share + self.common_electric_share + self.ev_charge_cost

    def __str__(self):
        return (f"{self.name}:\n"
                f"  Base Utils: ${self.base_utilities_share:.2f}\n"
                f"  Common Elec: ${self.common_electric_share:.2f}\n"
                f"  EV Charging: ${self.ev_charge_cost:.2f}\n"
                f"  TOTAL:      ${self.total_due():.2f}")
