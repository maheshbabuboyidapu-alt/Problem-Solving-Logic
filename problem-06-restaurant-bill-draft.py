item = input("Enter the food item name:")
q = int(input("Enter quantity of the food item:"))
price = int(input("Enter the price of food item:"))
tip_choice = int(input("Enter the type of tip 1.custom-tip or 2.percentage-tip or 3.no-tip(enter only(1/2/3)):"))
if tip_choice not in [1,2,3]:
    print(f"Invalid choice!")
    exit()

per=0
if tip_choice == 1:
    tip_p = int(input("Enter the amount of tip:"))
elif tip_choice == 2:
    tip_p =int(input("Enter the percentage number between 10% or 15% or 20%:"))
    if tip_p not in [10,15,20]:
        print("Invalid percentage!")
        exit()
    per = tip_p / 100
    
member = input("Are you regular or non member:")
food_amount = q * price
print(f"Food amount:{q}X${price:.2f}=${food_amount:.2f}")
e_dis=0
if food_amount > 5000:
    e_dis = food_amount * 0.05
    print(f"Discount:5%=-${e_dis:.2f}")
else:
    print("Discount:None")
food_amount -= e_dis
print(f"Subtotal after discount:${food_amount:.2f}")
m_dis=0
if member.lower() == "regular":
    m_dis = food_amount * 0.1
    print(f"Member discount:10%=-${m_dis:.2f}")
else:
    print("Member discount:None")
food_amount -= m_dis
print(f"Final subtotal:${food_amount:.2f}")
if food_amount < 500:
    tax_p = 0.05
    tax_n = 5
    tax = food_amount * tax_p
elif food_amount <= 2000:
    tax_p = 0.12
    tax_n = 12
    tax = food_amount * tax_p
elif food_amount > 2000:
    tax_p = 0.18
    tax_n = 18
    tax = food_amount * tax_p
print(f"tax:{tax_n}% of ${food_amount:.2f}=${tax:.2f}")
tip=0
if tip_choice == 1:
    tip=tip_p
    print(f"Tip:${tip:.2f}")
elif tip_choice == 2:   
    tip = food_amount * per
    print(f"Tip:{tip_p}% of ${food_amount:.2f}=${tip:.2f}")
elif tip_choice == 3:
    print("Tip:$0")   
final_bill=food_amount+tip+tax
print(f"Final bill : ${final_bill:.2f}")