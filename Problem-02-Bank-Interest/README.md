# Problem 02 — Bank Interest Calculator

## Problem

Calculate interest earned from an account balance using different interest rates for different balance ranges.

Higher balances can also receive a bonus, and the highest balance tier has a tax deduction.

## Real-World Scenario

This models a banking rule system where the benefit received by a customer changes according to the account balance.

## Concepts Applied

- User input
- Type conversion with `float()`
- `if / elif / else`
- Comparison operators
- Arithmetic calculations
- Percentage calculations
- Multiple business rules in sequence
- Formatted numeric output

## My Approach

I treated each account-balance range as a separate business rule. After identifying the correct range, I calculated the interest and then applied any additional bonus or tax required by that range.

The refactored solution keeps the same decision logic while improving names, constants, formatting, and readability.

## What I Learned

- How to represent tier-based financial rules with conditional logic.
- How to apply multiple calculations in the correct order.
- How small changes in a requirement can change the final result.
- How clearer constants make financial calculations easier to follow.
