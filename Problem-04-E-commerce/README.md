# Problem 04 — E-Commerce Billing System

## Problem

Calculate the final payable amount for an online order using:

- Product category
- Order amount
- Category discount
- Bonus discount
- Shipping charge
- `SAVE10` coupon

## Real-World Scenario

This models an e-commerce checkout system where multiple pricing rules are applied in a specific order before the customer sees the final amount.

## Concepts Applied

- User input
- String normalization with `.lower()` and `.upper()`
- Input validation
- `if / elif / else`
- Membership-style category checking with lists
- Comparison and logical operators
- Percentage and arithmetic calculations
- Sequential business-rule processing
- Formatted output
- Early program exit with `exit()`

## My Approach

I processed the order step by step:

1. Validate the product category and order amount.
2. Apply the category-based discount.
3. Apply the bonus discount based on the discounted amount.
4. Calculate shipping according to the resulting amount.
5. Check whether the coupon is eligible.
6. Display the final payable amount.

The refactored version improves naming, structure, formatting, and readability while preserving the same business flow.

## What I Learned

- How to translate an e-commerce checkout requirement into ordered calculations.
- How the result of one rule can become the input to the next rule.
- How validation prevents invalid values from continuing through the calculation.
- How to keep several related business rules organized in one program.
