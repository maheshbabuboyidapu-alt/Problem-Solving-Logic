# Problem 10 — Department Payroll Breakdown

## Problem Statement

Process payroll grouped by department and generate a department-wise summary report.

## Salary Rules

- Up to 40 hours: normal hourly rate
- Hours beyond 40: 1.5× normal hourly rate

## Report Requirements

For each department, calculate:

- Individual salary of every employee
- Total department payroll
- Highest-paid employee
- Lowest-paid employee

## Input/Data

Each employee record contains name, department, hours worked, and hourly rate.

## Constraints

- Departments must be discovered dynamically from the data.
- Overtime is exactly 1.5× the normal rate.
- Only hours beyond 40 count as overtime.
