# Problem 06 — Restaurant Bill Calculator

## Problem

Calculate a restaurant bill from:

- Food item quantity and price
- Amount-based discount
- Membership discount
- Tax tier
- Tip choice

The tip can be a custom amount, a percentage, or no tip.

## Real-World Scenario

This models a restaurant checkout process where the final bill depends on several customer choices and amount-based rules.

## Concepts Applied

- User input
- Type conversion with `int()`
- Input validation
- Lists for valid choices
- `if / elif / else`
- String normalization with `.lower()`
- Arithmetic calculations
- Percentage calculations
- Multiple calculation stages
- Formatted output
- Early program exit with `exit()`

## My Approach

I built the bill in stages:

1. Validate the tip choice and percentage when required.
2. Calculate the food amount.
3. Apply the amount-based discount.
4. Apply the regular-member discount.
5. Calculate tax from the discounted subtotal.
6. Calculate the selected tip.
7. Add subtotal, tax, and tip to produce the final bill.

## What I Learned

- How to handle multiple user choices inside one business process.
- How calculation order changes the result of discounts, tax, and tips.
- How to use conditions to model different customer choices.
- How to keep a multi-step financial calculation understandable.
