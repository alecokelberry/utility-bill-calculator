"""
test_calculator.py
------------------
Unit tests for the UtilityCalculator cost-splitting logic.
"""

import unittest
import sys
import io
from calculator import UtilityCalculator
from models import Resident


class TestUtilityCalculator(unittest.TestCase):
    """Verifies weighted splitting, EV deduction, and balance checks."""

    def setUp(self):
        """Configure a standard test scenario: one couple and one single resident."""
        self.calc = UtilityCalculator()

        self.calc.residents = [
            Resident(name="Couple", split_weight=2.0),
            Resident(name="Single", split_weight=1.0),
        ]

        self.calc.costs = {
            "water": 30.0,
            "waste": 60.0,
            "storm": 10.0,
            "transport": 0.0,
            "electric_total": 100.0,
        }

        self.calc.ev_usage = [
            {"users": [0], "kwh": 100.0, "rate": 0.10}  # $10 EV cost for Couple
        ]

    def test_resident_setup(self):
        """Ensure residents are correctly configured."""
        self.assertEqual(len(self.calc.residents), 2)
        self.assertEqual(self.calc.residents[0].name, "Couple")
        self.assertEqual(self.calc.residents[0].split_weight, 2.0)
        self.assertEqual(self.calc.residents[1].name, "Single")
        self.assertEqual(self.calc.residents[1].split_weight, 1.0)
        self.assertEqual(self.calc.costs["water"], 30.0)

    def test_base_utilities_split(self):
        """Base utilities should split proportionally by weight."""
        self._run_calculate()

        # Base Total = 100.0, Total Weight = 3.0
        # Couple (weight 2.0) = 66.67, Single (weight 1.0) = 33.33
        self.assertAlmostEqual(self.calc.residents[0].base_utilities_share, 66.66666, places=4)
        self.assertAlmostEqual(self.calc.residents[1].base_utilities_share, 33.33333, places=4)

    def test_ev_cost_assignment(self):
        """EV costs should be assigned only to the specified residents."""
        self._run_calculate()

        # $10 EV cost assigned entirely to Couple (index 0)
        self.assertAlmostEqual(self.calc.residents[0].ev_charge_cost, 10.0)
        self.assertEqual(self.calc.residents[1].ev_charge_cost, 0.0)

    def test_common_electric_split(self):
        """Remaining electric (after EV deduction) should split by weight."""
        self._run_calculate()

        # Common Electric = 100.0 - 10.0 = 90.0
        # Per weight = 90.0 / 3.0 = 30.0
        # Couple = 60.0, Single = 30.0
        self.assertAlmostEqual(self.calc.residents[0].common_electric_share, 60.0)
        self.assertAlmostEqual(self.calc.residents[1].common_electric_share, 30.0)

    def test_total_due(self):
        """Each resident's total should be the sum of all their shares."""
        self._run_calculate()

        self.assertAlmostEqual(self.calc.residents[0].total_due(), 136.66666, places=4)
        self.assertAlmostEqual(self.calc.residents[1].total_due(), 63.33333, places=4)

    def test_balance_check(self):
        """Total collected across all residents should equal the actual bill total."""
        self._run_calculate()

        total_collected = sum(r.total_due() for r in self.calc.residents)
        actual_total = sum(self.calc.costs.values())
        self.assertAlmostEqual(total_collected, actual_total, places=2)

    def _run_calculate(self):
        """Helper to run calculate() while suppressing stdout."""
        captured = io.StringIO()
        sys.stdout = captured
        self.calc.calculate()
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
