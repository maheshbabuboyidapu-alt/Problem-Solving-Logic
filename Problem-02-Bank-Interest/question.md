# Problem 02 — Bank Interest Calculator

## Problem Statement

Calculate the interest earned from a bank account balance.

## Interest Rules

- Balance ≤ 0: invalid balance
- Balance ≤ ₹10,000: 2% interest
- Balance ≤ ₹50,000: 4% interest
- Balance ≤ ₹1,00,000: 6% interest + ₹500 bonus
- Balance > ₹1,00,000: 8% interest + ₹500 bonus, then 5% tax on the total interest

## Input

Enter the account balance.

## Example

**Input:** `75000`

**Expected output:** `Interest earned is ₹4500.00`

## Constraints

- Balance must be positive.
- Tax applies only to the highest balance tier.
- Round the final result to 2 decimal places.
