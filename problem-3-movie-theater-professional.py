"""
Movie Theater Ticket Pricing System

Description:
This program calculates the final ticket price based on customer age,
number of tickets purchased, show time, and membership status.

Pricing Structure:
Age Groups:
- Child (0-12 years)     : ₹150 per ticket
- Teen (13-17 years)     : ₹200 per ticket
- Adult (18-60 years)    : ₹300 per ticket
- Senior (61+ years)     : ₹200 per ticket

Time-Based Adjustments:
- Matinee (10 AM - 4:59 PM)  : -₹50
- Evening (5 PM - 8:59 PM)   : +₹100
- Night (9 PM - 11:59 PM)    : +₹150

Group Discounts (Applied after time adjustment):
- Less than 5 tickets    : No discount
- 5-9 tickets            : 10% discount
- 10-19 tickets          : 15% discount
- 20+ tickets            : 20% discount

Membership Discount (Applied last):
- Member                 : Additional 5% discount
- Non-member             : No additional discount
"""

# -------------------------------
# User Input
# -------------------------------

a = int(input("Enter age: "))
n = int(input("No. of tickets: "))
s_t = int(input("Show time: "))
m = input("Do you have membership? (Yes/No): ")

# -------------------------------
# Constants - Age Based Prices
# -------------------------------

child_price = 150
teen_price = 200
adult_price = 300
senior_price = 200

# -------------------------------
# Constants - Time Based Adjustments
# -------------------------------

matinee = -50
evening = 100
night = 150

# -------------------------------
# Constants - Discount Rates (Decimal)
# -------------------------------

per5 = 0.05
per10 = 0.10
per15 = 0.15
per20 = 0.20

# -------------------------------
# Constants - Discount Percentages (Display)
# -------------------------------

per_5 = 5
per_10 = 10
per_15 = 15
per_20 = 20

# -------------------------------
# Step 1: Determine Base Price by Age
# -------------------------------

if a > 0 and a <= 12:
    price = child_price
elif a > 12 and a <= 17:
    price = teen_price
elif a > 17 and a <= 60:
    price = adult_price
elif a > 60 and a < 120:
    price = senior_price

print(f"Base price: ${price}")

# -------------------------------
# Step 2: Apply Time-Based Adjustment
# -------------------------------

time_adj = 0
if s_t >= 10 and s_t < 17:
    time_adj += matinee
elif s_t >= 17 and s_t < 21:
    time_adj += evening
elif s_t >= 21 and s_t < 24:
    time_adj += night

# Display operator (+ for positive, empty for negative)
operator = ""
if time_adj > 0:
    operator = "+"

print(f"Time adjustment: ${operator}{time_adj}")
price += time_adj
print(f"Price after time adjustment: ${price}")

# -------------------------------
# Step 3: Apply Group Discount
# -------------------------------

g_dis = 0  # Discount amount (initially 0)
dis = None # Discount percentage (initially None)

# Determine discount tier based on ticket quantity
if n < 5:
    # Less than 5 tickets: No group discount
    pass
elif n >= 5 and n < 10:
    # 5-9 tickets: 10% discount
    g_dis = price * per10
    dis = per_10
elif n >= 10 and n < 20:
    # 10-19 tickets: 15% discount
    g_dis = price * per15
    dis = per_15
elif n >= 20:
    # 20+ tickets: 20% discount (maximum discount)
    g_dis = price * per20
    dis = per_20

# Display group discount result
if n < 5:
    print("Group discount: None")
else:
    print(f"Group discount: {dis}% = ${g_dis}")

# Apply discount to price
price -= g_dis
print(f"Price after group discount: ${price}")

# -------------------------------
# Step 4: Apply Membership Discount
# -------------------------------

m_dis = 0
if m.lower() == "yes":
    m_dis = price * per5
    price -= m_dis
    print(f"Membership discount: {per_5}% = ${m_dis}")
else:
    print(f"Membership discount: {m_dis}")

# -------------------------------
# Final Output
# -------------------------------

print(f"Final price per ticket: ${price}")
print(f"Total for {n} tickets: ${price * n}")