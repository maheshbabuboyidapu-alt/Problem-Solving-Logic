# Problem 03 — Movie Theater Ticket Pricing

## Problem Statement

Calculate the total ticket price for a movie theater booking.

## Pricing Rules

### Age-based base price
- Child (1–12): ₹150
- Teen (13–17): ₹200
- Adult (18–60): ₹300
- Senior (61+): ₹200

### Show-time adjustment
- Matinee (10:00–16:59): −₹50
- Evening (17:00–20:59): +₹100
- Night (21:00–23:59): +₹150

### Group discount
- Less than 5 tickets: 0%
- 5–9 tickets: 10%
- 10–19 tickets: 15%
- 20+ tickets: 20%

### Membership discount
- Member: 5%
- Non-member: 0%

Membership discount is applied after the group discount.

## Input

Enter age, number of tickets, show time in 24-hour format, and membership (Yes/No).

## Example

Age `25`, tickets `10`, show time `19`, member `Yes` produces a final price of ₹323 per ticket and ₹3230 total.
