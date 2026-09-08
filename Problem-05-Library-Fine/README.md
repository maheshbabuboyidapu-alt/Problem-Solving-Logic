# Problem 05 — Library Fine Calculator

## Problem

Calculate a library fine using:

- Number of overdue days
- Book type
- Membership status

The fine uses multiple overdue tiers, a book-type multiplier, a membership discount, and a maximum fine cap.

## Real-World Scenario

This models a library billing policy where different conditions change the amount a borrower must pay.

## Concepts Applied

- User input
- `try / except` validation for numeric input
- String normalization with `.lower()`
- Lists for valid input choices
- `if / elif / else`
- Comparison operators
- Arithmetic and percentage calculations
- Tiered calculations
- Sequential business-rule processing
- Final value capping
- Formatted output

## My Approach

I split the requirement into stages:

1. Validate overdue days.
2. Validate book type and membership.
3. Calculate the overdue fine across the applicable day tiers.
4. Apply the book-type multiplier.
5. Apply the membership discount.
6. Apply the maximum fine cap.

## What I Learned

- How to calculate a value across multiple ranges instead of treating every range as a separate final amount.
- How to handle invalid input before continuing with a calculation.
- How to apply multiplication, discounts, and caps in a controlled order.
- How real-world rules can be converted into a sequence of conditional decisions.
