# Utility Bill Calculator

A Python CLI application that fairly splits monthly utility bills among multiple residents. Supports weighted splits for couples and deducts individual electric vehicle (EV) charging costs before distributing the remaining electric bill.

---

## Features

- **Weighted Billing** — Distributes shared costs proportionally based on household size (e.g., a couple counts as two shares).
- **EV Charging Support** — Deducts specific EV charging costs from the total electric bill before splitting the remainder among all residents.
- **Couple Grouping** — Automatically combines couples into a single line item on the final report for cleaner output.
- **Detailed Reporting** — Generates a clear per-resident breakdown of base utilities, common electric, and EV charges with a built-in balance check.
- **Unit Tested** — Includes a test suite verifying the weighted splitting and EV deduction math.

---

## Project Structure

```
├── main.py            # CLI entry point
├── calculator.py      # Core splitting logic and interactive prompts
├── models.py          # Resident dataclass
├── utils.py           # Input validation helpers
└── tests/
    └── test_calculator.py
```

---

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

---

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

---

## Testing

Run the test suite with Python's built-in `unittest` framework:

```bash
python3 -m unittest discover tests/
```

---

## Development Approach — AI-Assisted Prototyping

This project is a deliberate showcase of how the next generation of developers can leverage AI coding assistants not as a crutch, but as a force multiplier — moving faster, shipping cleaner code, and solving harder problems than would otherwise be possible solo.

### My Philosophy

I supervise AI tools the same way a lead engineer supervises a junior developer: I define the architecture, set the requirements, review every line, and make all the final calls. The AI handles the boilerplate, accelerates iteration, and lets me stay focused on product thinking. The result is a faster feedback loop without sacrificing ownership of the codebase.

I completed WGU's Prompt Engineering course in a single day — a reflection of how fluent I've become working across multiple frontier models including Claude, Gemini, and Grok. Knowing how each model reasons, where each one excels, and how to structure prompts for each is a real and valuable skill — one I apply directly in projects like this.

### The AI Stack for This Project

**Phase 1 — Architecture & Planning with Grok 4.20 Beta**

The project outline, feature set, and initial architecture were developed using Grok 4.20 beta from [xAI](https://x.ai), accessed via the SuperGrok subscription. Grok 4.20 features a new rapid learning architecture with a 4-agent collaboration system where agents debate and fact-check each other to reduce hallucinations — an approach that makes it particularly strong for high-level planning and technical decisions. (xAI has also announced a "Heavy" tier featuring 16 specialized agents for even more demanding tasks.)

**Phase 2 — Implementation & Iteration in Google Antigravity IDE**

The bulk of implementation, feature development, debugging, and refinement was done inside [Google Antigravity IDE](https://antigravity.google) using Google DeepMind's latest models:

- **Gemini 3.1 Pro** — Long-context reasoning, cross-file refactors, and architectural decisions
- **Gemini 3.1 Flash** — Rapid back-and-forth feedback loops, quick edits, and fast iteration

Having access to multiple frontier models in a single IDE means I can route tasks to the right model for the job — the same way a senior engineer delegates to the right teammate.
