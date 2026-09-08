"""
Library Fine Calculator

Description:
This program calculates library fines based on book overdue days,
book type, and membership status with tiered pricing and caps.

Fine Structure:
- Days 1-7: ₹5/day
- Days 8-14: ₹10/day
- Days 15-30: ₹20/day
- Days 31+: ₹50/day

Book Type Multiplier:
- Fiction: 1x (no change)
- Non-Fiction: 1.5x (50% extra)
- Reference: 2x (double)

Membership Discount:
- Regular: 10% off
- Premium: 20% off
- Non-member: No discount

Maximum Fine Cap: ₹500
"""

# ===============================================
# Step 1: Input Validation
# ===============================================

# Get days overdue with error handling
try:
    days_overdue = int(input("Enter overdue days: "))
except ValueError:
    print("Error: Please enter a valid number for days overdue")
    exit()

# Validate days overdue is not negative
if days_overdue < 0:
    print("Error: Days overdue cannot be negative")
    exit()

# Get book type with validation
book_type = input("Enter book type (Fiction/Non-Fiction/Reference): ")
valid_book_types = ["fiction", "non-fiction", "reference"]
if book_type.lower() not in valid_book_types:
    print("Error: Invalid book type! Must be Fiction, Non-Fiction, or Reference")
    exit()

# Get membership status with validation
membership_status = input("Enter membership (Premium/Regular/Non-Member): ")
valid_memberships = ["premium", "regular", "non-member"]
if membership_status.lower() not in valid_memberships:
    print("Error: Invalid membership status! Must be Premium, Regular, or Non-Member")
    exit()

# ===============================================
# Step 2: Define Constants (Fine Tiers and Rates)
# ===============================================

# Tier 1: Days 1-7 at ₹5/day
tier_1_rate = 5
tier_1_limit = 7

# Tier 2: Days 8-14 at ₹10/day
tier_2_rate = 10
tier_2_limit = 14

# Tier 3: Days 15-30 at ₹20/day
tier_3_rate = 20
tier_3_limit = 30

# Tier 4: Days 31+ at ₹50/day
tier_4_rate = 50

# Maximum fine cap
maximum_fine_cap = 500

# ===============================================
# Step 3: Calculate Base Fine (Tiered Calculation)
# ===============================================

base_fine = 0.0

if days_overdue <= tier_1_limit:
    # All days fall in Tier 1
    base_fine = days_overdue * tier_1_rate
    print(f"Base fine: {days_overdue} days × ₹{tier_1_rate} = ₹{base_fine:.2f}")

elif days_overdue <= tier_2_limit:
    # Tier 1 (full) + Tier 2 (partial)
    tier_1_days = tier_1_limit
    tier_2_days = days_overdue - tier_1_limit
    base_fine = (tier_1_days * tier_1_rate) + (tier_2_days * tier_2_rate)
    print(f"Base fine: {tier_1_days} days × ₹{tier_1_rate} + {tier_2_days} days × ₹{tier_2_rate} = ₹{base_fine:.2f}")

elif days_overdue <= tier_3_limit:
    # Tier 1 (full) + Tier 2 (full) + Tier 3 (partial)
    tier_1_days = tier_1_limit
    tier_2_days = tier_2_limit - tier_1_limit
    tier_3_days = days_overdue - tier_2_limit
    base_fine = (tier_1_days * tier_1_rate) + (tier_2_days * tier_2_rate) + (tier_3_days * tier_3_rate)
    print(f"Base fine: {tier_1_days} days × ₹{tier_1_rate} + {tier_2_days} days × ₹{tier_2_rate} + {tier_3_days} days × ₹{tier_3_rate} = ₹{base_fine:.2f}")

else:
    # All tiers: Tier 1 (full) + Tier 2 (full) + Tier 3 (full) + Tier 4 (partial)
    tier_1_days = tier_1_limit
    tier_2_days = tier_2_limit - tier_1_limit
    tier_3_days = tier_3_limit - tier_2_limit
    tier_4_days = days_overdue - tier_3_limit
    base_fine = (tier_1_days * tier_1_rate) + (tier_2_days * tier_2_rate) + (tier_3_days * tier_3_rate) + (tier_4_days * tier_4_rate)
    print(f"Base fine: {tier_1_days} days × ₹{tier_1_rate} + {tier_2_days} days × ₹{tier_2_rate} + {tier_3_days} days × ₹{tier_3_rate} + {tier_4_days} days × ₹{tier_4_rate} = ₹{base_fine:.2f}")

# ===============================================
# Step 4: Apply Book Type Multiplier
# ===============================================

book_type_lower = book_type.lower()

if book_type_lower == "fiction":
    multiplier_value = 1.0
    multiplier_display = "1x"
elif book_type_lower == "non-fiction":
    multiplier_value = 1.5
    multiplier_display = "1.5x"
else:  # reference
    multiplier_value = 2.0
    multiplier_display = "2x"

base_fine *= multiplier_value
print(f"Book type multiplier: {book_type} ({multiplier_display}) = ₹{base_fine:.2f}")

# ===============================================
# Step 5: Apply Member Discount
# ===============================================

membership_lower = membership_status.lower()

if membership_lower == "non-member":
    discount_rate = 0.0
    discount_percentage = 0
elif membership_lower == "regular":
    discount_rate = 0.1
    discount_percentage = 10
else:  # premium
    discount_rate = 0.2
    discount_percentage = 20

member_discount_amount = base_fine * discount_rate
base_fine -= member_discount_amount
print(f"Membership discount: {discount_percentage}% = -₹{member_discount_amount:.2f}")
print(f"After discount: ₹{base_fine:.2f}")

# ===============================================
# Step 6: Apply Maximum Fine Cap
# ===============================================

if base_fine > maximum_fine_cap:
    base_fine = maximum_fine_cap

print(f"Final fine: ₹{base_fine:.2f}")