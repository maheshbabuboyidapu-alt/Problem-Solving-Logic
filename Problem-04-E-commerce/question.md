# Problem 04 — E-Commerce Order Calculator

## Problem Statement

Calculate the final order amount for an e-commerce purchase.

## Rules

### Category discount
- Electronics: 5%
- Clothing: 15%
- Books: 10%
- Groceries: 0%

### Bonus discount
Applied after the category discount:
- Below ₹1,000: 0%
- ₹1,000–₹4,999: 5%
- ₹5,000–₹9,999: 10%
- ₹10,000+: 15%

### Shipping
Applied after both discounts:
- Below ₹500: ₹100
- ₹500–₹1,999: ₹50
- ₹2,000+: Free

### Coupon
`SAVE10` is valid when the discounted order amount is above ₹1,000 and deducts ₹100.

## Input

Enter category, order amount, and coupon code.

## Constraints

- Category must be Electronics, Clothing, Books, or Groceries.
- Order amount must be greater than 0.
- Apply discounts in the stated order.
