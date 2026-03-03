"""
main.py
-------
Entry point for the Utility Bill Calculator.
Orchestrates the loading of data and execution of the calculator.
"""

import sys
from calculator import UtilityCalculator
from bills import load_dec_2025_jan_2026_data, load_jan_2026_feb_2026_data

def main():
    print("Welcome to the Utility Bill Calculator")
    
    calc = UtilityCalculator()
    
    # Check for arguments could be added here.
    # For now, default to the requested archived bill data.
    
    try:
        data = load_jan_2026_feb_2026_data()
        calc.load_data(data)
        calc.calculate()
        calc.print_report()
    except Exception as e:
        print(f"An error occurred during calculation: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
