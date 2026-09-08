# Problem 08 — Employee Overtime & Night Shift Pay

## Problem

Calculate an employee's daily payment from:

- Hourly rate
- Hours worked
- Workday type
- Night-shift status

The program separates regular hours, eligible overtime, overtime rate, and night-shift bonus.

## Real-World Scenario

This models payroll logic for employees whose overtime rate changes according to the day they worked.

## Concepts Applied

- User input
- Input validation
- String normalization with `.strip()` and `.lower()`
- Lists for valid choices
- Dictionaries for workday overtime multipliers
- `if / elif / else`
- `min()` and `max()` for hour limits
- Arithmetic and percentage-style calculations
- Sequential payroll calculation
- Formatted output

## My Approach

I separated the payroll calculation into clear stages:

1. Validate employee inputs.
2. Calculate regular pay for the first 8 hours.
3. Calculate overtime and cap eligible overtime at 4 hours.
4. Select the overtime multiplier based on the workday.
5. Calculate the night-shift bonus when applicable.
6. Add the components to produce the total payment.

## What I Learned

- How to model limits such as maximum eligible overtime.
- How a dictionary can connect a category to its corresponding calculation value.
- How to separate regular pay, overtime pay, and bonuses before combining them.
- How to turn a payroll policy into a sequence of measurable calculation steps.
