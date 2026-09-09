# Problem 08 — Overtime Pay Calculator

## Problem Statement

Calculate an employee's total pay including regular pay, overtime pay, and a night-shift bonus.

## Rules

- First 8 hours are regular hours.
- Hours beyond 8 are overtime, capped at 4 hours.
- Overtime multiplier:
  - Weekday: 1.5×
  - Saturday: 2.0×
  - Sunday: 2.5×
- Night-shift bonus applies only when overtime exists: overtime hours × ₹50.

## Input

Enter hourly rate, hours worked, day (Weekday/Saturday/Sunday), and night shift (Yes/No).

## Constraints

- Overtime is capped at 4 hours.
- Night bonus requires overtime.
