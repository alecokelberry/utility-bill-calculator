"""
models.py
---------
Defines the data structures for the Utility Bill Calculator.
"""

from dataclasses import dataclass

@dataclass
class Resident:
    """
    Represents a resident or billing entity.
    
    Attributes:
        name (str): The display name of the resident.
        split_weight (float): The weighting for shared costs (default 1.0).
        is_couple (bool): Whether this resident is part of a couple for grouped reporting.
        base_utilities_share (float): Calculated share of base utilities (Water, Waste, etc).
        common_electric_share (float): Calculated share of common electric costs.
        ev_charge_cost (float): Specific cost assigned for EV charging.
    """
    name: str
    split_weight: float = 1.0
    is_couple: bool = False
    base_utilities_share: float = 0.0
    common_electric_share: float = 0.0
    ev_charge_cost: float = 0.0

    def total_due(self) -> float:
        """Returns the total cost associated with this resident."""
        return self.base_utilities_share + self.common_electric_share + self.ev_charge_cost

    def __str__(self):
        return (f"{self.name}:\n"
                f"  Base Utils: ${self.base_utilities_share:.2f}\n"
                f"  Common Elec: ${self.common_electric_share:.2f}\n"
                f"  EV Charging: ${self.ev_charge_cost:.2f}\n"
                f"  TOTAL:      ${self.total_due():.2f}")

