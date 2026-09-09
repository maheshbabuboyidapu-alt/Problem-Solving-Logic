# Problem 06 — Restaurant Bill Calculator

## Problem Statement

Calculate the final restaurant bill for a customer.

## Rules

1. Food amount = quantity × price per item.
2. If food amount is above ₹5,000, apply a 5% bulk discount.
3. Regular members receive 10% after the bulk discount.
4. Tax is calculated on the final subtotal after discounts:
   - Below ₹500: 5%
   - ₹500–₹2,000: 12%
   - Above ₹2,000: 18%
5. Tip may be custom, 10%, 15%, 20%, or none. Percentage tip uses the subtotal after discounts and before tax.

## Input

Enter food item name, quantity, price per item, tip choice, and membership status.

## Constraints

- Tip percentage must be exactly 10, 15, or 20 when percentage tipping is selected.
- Discounts are applied before tax.
