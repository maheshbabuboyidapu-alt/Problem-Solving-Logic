"""
Parking Fee Calculator

Description:
This program calculates the parking fee based on the number of hours
a vehicle is parked in the parking area.

Parking Charges:
- First 2 hours      : ₹30 (Fixed)
- Next 3 hours       : ₹20 per hour
- After 5 hours      : ₹10 per additional hour
- If total fee > ₹200: 10% discount is applied
"""

# -------------------------------
# User Input
# -------------------------------

h = int(input("Enter the number of hours parked: "))

# -------------------------------
# Constants
# -------------------------------

BASE_RATE = 30       # Fixed charge for the first 2 hours
TIER2_RATE = 20      # Charge per hour from 3rd to 5th hour
TIER3_RATE = 10      # Charge per hour after 5 hours
DISCOUNT_RATE = 0.10 # 10% discount

# -------------------------------
# Parking Fee Calculation
# -------------------------------

# Invalid input
if h <= 0:
    print("Invalid parking hours.")

# Vehicle parked for up to 2 hours
elif h <= 2:
    print(f"Parking Fee: ₹{BASE_RATE}")

# Vehicle parked between 3 and 5 hours
elif h <= 5:
    tier2_hours = h - 2
    total_fee = BASE_RATE + (tier2_hours * TIER2_RATE)
    print(f"Parking Fee: ₹{total_fee}")

# Vehicle parked for more than 5 hours
else:
    tier2_total = 3 * TIER2_RATE
    tier3_hours = h - 5
    total_fee = BASE_RATE + tier2_total + (tier3_hours * TIER3_RATE)

    # Apply discount if fee exceeds ₹200
    if total_fee > 200:
        discount = total_fee * DISCOUNT_RATE
        total_fee -= discount
        print(f"Discount Applied: ₹{discount:.2f}")

    print(f"Parking Fee: ₹{total_fee:.2f}")