"""
Product Billing System

Description:
This program calculates the final payable amount for a customer's order.

Features:
- Validates product category and order amount
- Applies category-based discounts
- Applies bonus discounts based on the discounted order amount
- Calculates shipping charges
- Applies SAVE10 coupon (₹100 discount) for eligible orders
- Displays the final payable amount

Category Discounts:
- Electronics : 5%
- Clothing    : 15%
- Books       : 10%
- Groceries   : No discount

Bonus Discounts (After Category Discount):
- ₹1,000 - ₹4,999   : 5%
- ₹5,000 - ₹9,999   : 10%
- ₹10,000 and above : 15%

Shipping Charges:
- Below ₹500   : ₹100
- ₹500 - ₹1,999: ₹50
- ₹2,000+      : Free

Coupon:
- SAVE10 : ₹100 discount if amount after discounts exceeds ₹1000.
"""

# ---------------------------------
# User Input
# ---------------------------------

category = input("Enter category: ").lower()

if category not in ["electronics", "clothing", "books", "groceries"]:
    print("Invalid category!")
    exit()

order_amount = float(input("Enter order amount: "))

if order_amount <= 0:
    print("Invalid order amount!")
    exit()

coupon = input("Enter coupon: ").upper()

# ---------------------------------
# Constants
# ---------------------------------

ELECTRONICS_DISCOUNT = 0.05
CLOTHING_DISCOUNT = 0.15
BOOKS_DISCOUNT = 0.10

BONUS_5 = 0.05
BONUS_10 = 0.10
BONUS_15 = 0.15

SHIPPING_100 = 100
SHIPPING_50 = 50

COUPON_DISCOUNT = 100

# ---------------------------------
# Category Discount
# ---------------------------------

category_discount = 0
category_percent = 0

if category == "electronics":
    category_discount = order_amount * ELECTRONICS_DISCOUNT
    category_percent = 5

elif category == "clothing":
    category_discount = order_amount * CLOTHING_DISCOUNT
    category_percent = 15

elif category == "books":
    category_discount = order_amount * BOOKS_DISCOUNT
    category_percent = 10

if category == "groceries":
    print("Category Discount : None")
else:
    print(f"Category Discount : {category_percent}% = ₹{category_discount:.2f}")

order_amount -= category_discount
print(f"After Category Discount : ₹{order_amount:.2f}")

# ---------------------------------
# Bonus Discount
# ---------------------------------

bonus_discount = 0
bonus_percent = 0

if 1000 <= order_amount < 5000:
    bonus_discount = order_amount * BONUS_5
    bonus_percent = 5

elif 5000 <= order_amount < 10000:
    bonus_discount = order_amount * BONUS_10
    bonus_percent = 10

elif order_amount >= 10000:
    bonus_discount = order_amount * BONUS_15
    bonus_percent = 15

if bonus_discount == 0:
    print("Bonus Discount : None")
else:
    print(f"Bonus Discount : {bonus_percent}% = ₹{bonus_discount:.2f}")

order_amount -= bonus_discount
print(f"After Bonus Discount : ₹{order_amount:.2f}")

# Store amount before shipping
price_after_discount = order_amount

# ---------------------------------
# Shipping Charges
# ---------------------------------

shipping_charge = 0

if order_amount < 500:
    shipping_charge = SHIPPING_100

elif order_amount < 2000:
    shipping_charge = SHIPPING_50

if shipping_charge == 0:
    print("Shipping Charge : Free")
else:
    print(f"Shipping Charge : ₹{shipping_charge}")
    order_amount += shipping_charge

# ---------------------------------
# Coupon Discount
# ---------------------------------

if coupon == "SAVE10":

    if price_after_discount > 1000:
        print(f"Coupon Applied : SAVE10 = -₹{COUPON_DISCOUNT}")
        order_amount -= COUPON_DISCOUNT

    else:
        print("Coupon : Invalid")

else:
    print("Coupon : None")

# ---------------------------------
# Final Bill
# ---------------------------------

print(f"\nFinal Payable Amount : ₹{order_amount:.2f}")
