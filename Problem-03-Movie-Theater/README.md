# Problem 03 — Movie Theater Ticket Pricing

## Problem

Calculate the final price of movie tickets using:

- Customer age
- Number of tickets
- Show time
- Membership status

The price changes according to age and show time, followed by group and membership discounts.

## Real-World Scenario

This represents a ticket-pricing system where several customer and booking conditions affect the final amount.

## Concepts Applied

- User input
- Type conversion with `int()`
- String input and `.lower()`
- `if / elif / else`
- Comparison and logical operators
- Arithmetic calculations
- Percentage calculations
- Sequential business-rule processing
- Formatted output

## My Approach

I processed the ticket price in stages:

1. Determine the base price from age.
2. Apply the show-time adjustment.
3. Apply the group discount according to ticket quantity.
4. Apply the membership discount.
5. Calculate the total price for all tickets.

The refactored solution keeps this staged calculation flow while improving readability and organization.

## What I Learned

- How to combine several independent business rules into one calculation.
- How to process discounts in a defined order.
- How to reason about ranges such as age, show time, and ticket quantity.
- How to build a realistic pricing problem using only the concepts I had learned at this stage.
