# Problem 09 — Team Payroll Summary

## Problem

Calculate payroll for a team of employees and report:

- Individual employee salary
- Total payroll
- Average pay
- Highest-paid employee
- Number of employees who worked overtime

Each employee record contains a name, hours worked, and hourly rate.

## Real-World Scenario

This models a small payroll-processing system that works with multiple employee records instead of a single person's input.

## Concepts Applied

- Lists
- Dictionaries
- `for` loops
- Dictionary key access
- Conditional statements
- Arithmetic calculations
- Accumulator variables
- Counting and aggregation
- Finding a maximum value
- Average calculation
- Empty-data validation

## My Approach

I represented each employee as a dictionary and stored the team in a list. Then I looped through the employees and calculated each salary according to regular and overtime hours.

While processing the same list, I also accumulated total payroll, tracked the highest-paid employee, calculated the number of overtime employees, and finally calculated the average pay.

## What I Learned

- How lists and dictionaries can represent collections of real-world records.
- How one loop can calculate several useful summary values.
- How to track totals, counts, and maximum values while processing data.
- How a problem becomes more data-oriented when it moves from one employee to a team of employees.

## Development Note

This problem marks the transition in my repository from mainly rule-based single-case problems to problems that operate on collections of structured data.
