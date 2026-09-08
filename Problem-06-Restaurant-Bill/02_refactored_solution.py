"""
Restaurant Bill Calculator

Description:
This program calculates the final restaurant bill including food items,
applicable taxes, discounts, and tips based on customer choices and membership.

Pricing Structure:
- Food items: Quantity × Price per item

Discounts (Applied to food amount):
- Amount-based: 5% off if food > ₹5000
- Member-based: Additional 10% off if regular member

Tax (Applied to discounted amount):
- < ₹500: 5% tax
- ₹500-₹2000: 12% tax
- > ₹2000: 18% tax

Tip Options (Calculated on final subtotal after discounts):
- Custom amount: User enters fixed tip
- Percentage: 10%, 15%, or 20% of subtotal
- No tip: ₹0

Final Bill = Subtotal + Tax + Tip
"""

# ===============================================
# Step 1: User Input and Validation
# ===============================================

# Get food item details
item_name = input("Enter the food item name: ")
quantity = int(input("Enter quantity of the food item: "))
price_per_item = int(input("Enter the price of food item: "))

# Get tip choice with validation
tip_choice = int(input("Enter tip type (1.custom-tip / 2.percentage-tip / 3.no-tip): "))
if tip_choice not in [1, 2, 3]:
    print("Error: Invalid tip choice! Must be 1, 2, or 3")
    exit()

# Initialize tip percentage variable
tip_percentage = 0.0
tip_amount = 0

# Handle tip choice
if tip_choice == 1:
    # Custom tip amount
    tip_amount = int(input("Enter the tip amount in rupees: "))
elif tip_choice == 2:
    # Percentage-based tip
    tip_percentage = int(input("Enter tip percentage (10 / 15 / 20): "))
    if tip_percentage not in [10, 15, 20]:
        print("Error: Invalid percentage! Must be 10, 15, or 20")
        exit()
    tip_percentage = tip_percentage / 100

# Get membership status
membership_status = input("Are you regular or non-member: ")

# ===============================================
# Step 2: Calculate Food Amount
# ===============================================

food_amount = quantity * price_per_item
print(f"Food amount: {quantity} × ${price_per_item:.2f} = ${food_amount:.2f}")

# ===============================================
# Step 3: Apply Amount-Based Discount (> ₹5000)
# ===============================================

amount_discount = 0.0
if food_amount > 5000:
    amount_discount = food_amount * 0.05
    print(f"Discount: 5% = -${amount_discount:.2f}")
else:
    print("Discount: None")

food_amount -= amount_discount
print(f"Subtotal after discount: ${food_amount:.2f}")

# ===============================================
# Step 4: Apply Member Discount (10% for regular)
# ===============================================

member_discount = 0.0
if membership_status.lower() == "regular":
    member_discount = food_amount * 0.1
    print(f"Member discount: 10% = -${member_discount:.2f}")
else:
    print("Member discount: None")

food_amount -= member_discount
print(f"Final subtotal: ${food_amount:.2f}")

# ===============================================
# Step 5: Calculate Tax (Tiered Based on Amount)
# ===============================================

tax_rate = 0.0
tax_percentage = 0

if food_amount < 500:
    tax_rate = 0.05
    tax_percentage = 5
elif food_amount <= 2000:
    tax_rate = 0.12
    tax_percentage = 12
else:  # food_amount > 2000
    tax_rate = 0.18
    tax_percentage = 18

tax_amount = food_amount * tax_rate
print(f"Tax: {tax_percentage}% of ${food_amount:.2f} = ${tax_amount:.2f}")

# ===============================================
# Step 6: Calculate Tip (Based on Customer Choice)
# ===============================================

if tip_choice == 1:
    # Custom tip amount (already set from user input)
    print(f"Tip: ${tip_amount:.2f}")
elif tip_choice == 2:
    # Percentage-based tip (calculated on final subtotal)
    tip_amount = food_amount * tip_percentage
    print(f"Tip: {int(tip_percentage * 100)}% of ${food_amount:.2f} = ${tip_amount:.2f}")
else:  # tip_choice == 3
    # No tip
    tip_amount = 0
    print("Tip: $0")

# ===============================================
# Step 7: Calculate Final Bill
# ===============================================

final_bill = food_amount + tax_amount + tip_amount
print(f"Final bill: ${final_bill:.2f}")