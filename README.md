# Utility Bill Calculator

A flexible Python application designed to split utility bills among multiple residents, featuring support for weighted splits (e.g., couples) and specific electric vehicle (EV) charging costs.

## Description

This tool automates the process of calculating monthly utility splits. It takes into account:

- **Base Utilities**: Water, Waste, Storm, and Transportation fees.
- **Electricity**: Separates common usage from individual EV charging costs.
- **Weighted Splitting**: Allows assigning weights to residents (e.g., a single person = 1.0, a couple = 2.0) to ensure fair distribution of shared costs.

## Features

- **Weighted Billing**: Fairly distributes common costs based on household size.
- **EV Charging Support**: Deducts specific EV charging costs from the total electric bill before splitting the remainder.
- **Detailed Reporting**: Generates a clear breakdown of costs for each resident, including base utilities, common electric, and EV charges.
- **Extensible Data Loading**: Uses a separate module (`bills.py`) to manage bill data, allowing for easy archiving of past months.

## Project Structure

- `main.py`: Entry point. Loading data and running the calculator.
- `calculator.py`: Core logic for cost splitting and managing residents.
- `models.py`: Data structures (e.g., `Resident` class).
- `bills.py`: Data file containing configuration for specific billing periods.
- `utils.py`: Helper functions for input handling.

## Usage

To run the calculator with the default configuration (Dec 2025 - Jan 2026 data):

```bash
python3 main.py
```

### Modifying Data

To calculate for a new month, edit or add a new function in `bills.py` with the relevant costs and resident setup, then update `main.py` to call that function.

## Example Output

```text
========================================
 FINAL BILL REPORT
========================================
Resident 1 & 2 (Couple):
  Base Utils: $80.88
  Common Elec: $51.09
  EV Charging: $24.48
  TOTAL:      $156.45
--------------------
...
Total Collected: $307.75
Actual Bill Total: $307.75
Balance Check: OK
```
