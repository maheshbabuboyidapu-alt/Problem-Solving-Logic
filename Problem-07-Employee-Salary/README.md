# Problem 07 — Employee Salary & Bonus Calculator

## Problem

Calculate an employee's final salary using:

- Years of experience
- Performance rating
- Attendance percentage
- Performance bonus
- Attendance penalty
- Tax deduction

## Real-World Scenario

This models a payroll rule system in which several employee attributes affect the final take-home salary.

## Concepts Applied

- User input
- Input validation
- Lists for valid rating choices
- String normalization with `.lower()`
- `if / elif / else`
- Comparison and logical operators
- Percentage calculations
- Sequential calculations
- Formatted output
- Early program exit with `exit()`

## My Approach

I processed the salary in a fixed sequence:

1. Validate experience, rating, and attendance.
2. Select the base salary from the experience range.
3. Calculate the performance bonus.
4. Apply the attendance penalty.
5. Determine the applicable tax rate.
6. Calculate the final take-home salary.

## What I Learned

- How several employee rules can work together to produce one result.
- How the output of one stage becomes the input to the next stage.
- How to translate HR-style policies into conditional logic.
- How validation and ordered calculations make business logic easier to reason about.
