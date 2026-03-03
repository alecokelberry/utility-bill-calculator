# Utility Bill Calculator

A Python CLI application that fairly splits monthly utility bills among multiple residents. Supports weighted splits for couples and deducts individual electric vehicle (EV) charging costs before distributing the remaining electric bill.

## Features

- **Weighted Billing** — Distributes shared costs proportionally based on household size (e.g., a couple counts as two shares).
- **EV Charging Support** — Deducts specific EV charging costs from the total electric bill before splitting the remainder among all residents.
- **Couple Grouping** — Automatically combines couples into a single line item on the final report for cleaner output.
- **Detailed Reporting** — Generates a clear per-resident breakdown of base utilities, common electric, and EV charges with a built-in balance check.
- **Unit Tested** — Includes a test suite verifying the weighted splitting and EV deduction math.

## Project Structure

```
├── main.py            # CLI entry point
├── calculator.py      # Core splitting logic and interactive prompts
├── models.py          # Resident dataclass
├── utils.py           # Input validation helpers
└── tests/
    └── test_calculator.py
```

## Usage

Run the interactive calculator:

```bash
python3 main.py
```

The program will walk you through:

1. **Residents** — Enter the number of residents and their names.
2. **Couples** — Identify any couples by their resident index to adjust split weights.
3. **Bills** — Enter each utility line item: Electric Meter, Transportation, Water Meter, Waste Water, Storm Water, and Solid Waste.
4. **EV Charging** — Optionally enter EV charging details (kWh and rate) and assign them to specific residents.

## Example Output

```text
Welcome to the Utility Bill Calculator

Total Billing Weights: 4.0

========================================
 FINAL BILL REPORT
========================================
Alec & Brook:
  Base Utils: $80.88
  Common Elec: $42.18
  EV Charging: $29.25
  TOTAL:      $152.31
--------------------
Austin:
  Base Utils: $40.44
  Common Elec: $21.09
  EV Charging: $17.50
  TOTAL:      $79.03
--------------------
Adrien:
  Base Utils: $40.44
  Common Elec: $21.09
  EV Charging: $0.00
  TOTAL:      $61.53
--------------------
Total Collected: $292.87
Actual Bill Total: $292.87
Balance Check: OK
```

## Testing

Run the test suite with Python's built-in `unittest` framework:

```bash
python3 -m unittest discover tests/
```
