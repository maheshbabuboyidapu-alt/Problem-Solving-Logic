category = input("Enter category of the product [Electronics, Clothing, Books, Groceries]: ")

if category.lower() != "electronics" and \
   category.lower() != "clothing" and \
   category.lower() != "books" and \
   category.lower() != "groceries":
    print("Invalid category!")
    exit()
order_amount=int(input("Enter order amount of the product():"))
if order_amount==0 or order_amount<0:
    print("Invalid order amount")
    exit()
    
coupon=input("Enter coupon:")
# persentages
five_p=0.05
fifteen_p=0.15
ten_p=0.10
#%numbers
five_5=5
fifteen_15=15
ten_10=10

#shipping cost
shipping_a=100
shipping_b=50

#coupon 
save10=-100

# Discount based on category
c_dis=0
category_dis=0.0
if category.lower()=="electronics":
    category_dis=order_amount*five_p
    c_dis=five_5
elif category.lower()=="clothing":
    category_dis=order_amount*fifteen_p
    c_dis=fifteen_15
elif category.lower()=="books":
    category_dis=order_amount*ten_p
    c_dis=ten_10    
     
if category.lower() =="groceries":
    print("Category discount:None")
else:           
    print(f"Category discount:{c_dis}%=${category_dis}")

order_amount-=category_dis
print(f"After category discount:${order_amount}")
#bonus discount based on order amount(after discount)
bonus_dis=0
b_dis=0
if order_amount>=1000 and order_amount<5000:
    bonus_dis=order_amount*five_p
    b_dis=five_5
elif order_amount>=5000 and order_amount<10000:
    bonus_dis=order_amount*ten_p
    b_dis=ten_10
elif order_amount>10000:
    bonus_dis=order_amount*fifteen_p
    b_dis=fifteen_15        
    
if order_amount >=0 and order_amount<1000:
   print("Bonus discount:None")
else:
   print(f"Bonus discount:{b_dis}%=${bonus_dis}")   
    
order_amount-=bonus_dis
print(f"After bonus discount:${order_amount}")
price=order_amount

# Shipping cost (based on final price after discounts)
shipping_cost=0
if order_amount<500:
    shipping_cost+=shipping_a
elif order_amount<2000:
    shipping_cost+=shipping_b
        
if order_amount>=2000:
    print("Shipping cost:Free")    
else:
    print(f"Shipping cost:${shipping_cost}")    
    order_amount+=shipping_cost


c=order_amount-price
                
if coupon == "SAVE10" and price>1000:   
    print(f"Coupon:{coupon} valid =${save10}")    
    price+=save10
elif coupon == "SAVE10" and         price<=1000:
    print("Coupon:Invalid")
else:
    print("Coupon:None")    

price+=c                
print(f"Final amount:${price}")  