"""
utils.py
--------
Helper functions for input handling.
"""

def get_float_input(prompt: str, default: float = None) -> float:
    """
    Prompts the user for a float input. 
    Returns `default` if input is empty and default is provided.
    """
    while True:
        try:
            user_in = input(prompt)
            if not user_in and default is not None:
                return default
            return float(user_in)
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_int_input(prompt: str) -> int:
    """Prompts the user for an integer input."""
    while True:
        try:
            val = input(prompt)
            return int(val)
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_bool_input(prompt: str) -> bool:
    """Prompts the user for a yes/no input and returns a boolean."""
    while True:
        val = input(prompt).strip().lower()
        if val in ['y', 'yes', 'true', '1']:
            return True
        elif val in ['n', 'no', 'false', '0']:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
