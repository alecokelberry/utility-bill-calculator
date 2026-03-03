"""
main.py
-------
Entry point for the Utility Bill Calculator.
Runs an interactive CLI session to configure residents and calculate splits.
"""

import sys
from calculator import UtilityCalculator

def main():
    print("Welcome to the Utility Bill Calculator")
    
    calc = UtilityCalculator()
    
    # Interactive Mode
    try:
        calc.interactive_setup_residents()
        calc.interactive_input_costs()
        calc.interactive_input_ev()
        
        calc.calculate()
        calc.print_report()
    except KeyboardInterrupt:
        print("\nSetup cancelled.")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
