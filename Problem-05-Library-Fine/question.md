# Problem 05 — Library Fine Calculator

## Problem Statement

Calculate the library fine for a book returned late.

## Fine Rules

- Days 1–7: ₹5 per day
- Days 8–14: ₹10 per day for days beyond 7
- Days 15–30: ₹20 per day for days beyond 14
- Days 31+: ₹50 per day for days beyond 30

## Book Type Multiplier
- Fiction: 1×
- Non-fiction: 1.5×
- Reference: 2×

## Membership Discount
- Non-member: 0%
- Regular: 10%
- Premium: 20%

Maximum fine: ₹500.

## Input

Enter days overdue, book type, and membership status.

## Constraints

- Days overdue must be 0 or greater.
- Fine tiers are cumulative.
- Final fine is capped at ₹500.
