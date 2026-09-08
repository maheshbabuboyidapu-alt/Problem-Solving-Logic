# Problem 01 — Parking Fee Calculator

## Problem

Build a parking fee calculator based on the number of hours a vehicle is parked.

The fee follows different pricing tiers:

- First 2 hours: fixed ₹30
- Hours 3–5: ₹20 per additional hour
- After 5 hours: ₹10 per additional hour
- If the calculated fee is above ₹200, apply a 10% discount

## Real-World Scenario

This models the type of rule-based pricing system used in a parking facility, where the final charge depends on how long a customer uses the service.

## Concepts Applied

- Variables and numeric values
- User input
- Type conversion with `int()`
- `if / elif / else`
- Comparison operators
- Arithmetic calculations
- Nested conditional logic
- Formatted output

## My Approach

I converted the parking rules into separate time-based conditions. Each condition calculates the charge for the corresponding parking range. For longer stays, I added the higher-hour charge and then checked whether the total qualified for the discount.

The refactored solution makes the same rules clearer by using descriptive constants and a more structured calculation flow.

## What I Learned

- How to translate tiered pricing rules into conditions.
- How to break a real-world calculation into smaller decision stages.
- How boundary conditions such as 2 hours, 5 hours, and ₹200 affect the result.
- How clearer variable names and constants make a solution easier to understand.
