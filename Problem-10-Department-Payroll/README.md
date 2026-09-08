# Problem 10 — Department Payroll Breakdown

## Problem

Calculate payroll department by department and report:

- Individual employee salary
- Total department payroll
- Highest-paid employee in each department
- Lowest-paid employee in each department

The employee data contains a name, department, hours worked, and hourly rate.

## Real-World Scenario

This models a company payroll report where the same payroll rules must be applied separately to every department.

## Concepts Applied

- Lists
- Dictionaries
- `set` for unique department tracking
- `for` loops
- Nested iteration
- Dictionary key access
- Conditional statements
- Functions in the initial solution
- Arithmetic calculations
- Accumulator variables
- Highest/lowest value tracking
- Grouped data processing

## My Approach

I first identified the unique departments from the employee data. Then I processed the employees belonging to each department and calculated salary using the overtime rule.

For every department, I maintained its own payroll total and tracked both the highest-paid and lowest-paid employee.

The initial solution introduced a reusable `cs(hours, rate)` function for the salary calculation. The refactored solution focuses on a clearer step-by-step structure and descriptive names.

## What I Learned

- How to move from team-level processing to grouped processing.
- How lists and dictionaries can represent structured business data.
- How a set can help identify unique categories such as departments.
- How nested loops can process records group by group.
- How to track both maximum and minimum values while processing data.
- How reusable functions can separate a repeated calculation from the main processing flow.

## Improvement From Problem 09

Problem 09 processes one team as a single collection. In this problem, I extended the idea to a second level: employees are processed according to their department, and each department receives its own summary.
