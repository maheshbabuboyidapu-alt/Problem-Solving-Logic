a = int(input("Enter age: "))
n = int(input("No. of tickets: "))
s_t = int(input("Show time: "))
m = input("Do you have membership? (Yes/No): ")

# Age based prices
child_price = 150
teen_price = 200
adult_price = 300
senior_price = 200

# Time based pricing
matinee = -50
evening = 100
night = 150

# Discounts
per5 = 0.05
per10 = 0.10
per15 = 0.15
per20 = 0.20

# Percentages
per_5 = 5
per_10 = 10
per_15 = 15
per_20 = 20

# Prices based on age
if a > 0 and a <= 12:
    price = child_price
elif a > 12 and a <= 17:
    price = teen_price
elif a > 17 and a <= 60:
    price = adult_price
elif a > 60 and a < 120:
    price = senior_price

print(f"Base price: ${price}")

# Prices based on show time
time_adj = 0
if s_t >= 10 and s_t < 17:
    time_adj += matinee
elif s_t >= 17 and s_t < 21:
    time_adj += evening
elif s_t >= 21 and s_t < 24:
    time_adj += night

# Handling the operator problem
operator = ""
if time_adj > 0:
    operator = "+"

print(f"Time adjustment: ${operator}{time_adj}")
price += time_adj
print(f"Price after time adjustment: ${price}")

# Prices based on group
g_dis = 0
dis = None
if n < 5:
    print("Group discount: None")
elif n > 4 and n < 10:
    g_dis += price * per10
    dis = per_10
    print(f"Group discount: {dis}% = ${g_dis}")
elif n > 9 and n < 20:
    g_dis += price * per15
    dis = per_15
    print(f"Group discount: {dis}% = ${g_dis}")
elif n >= 20:
    g_dis += price * per20
    dis = per_20
    print(f"Group discount: {dis}% = ${g_dis}")

price -= g_dis
print(f"Price after group discount: ${price}")

# Adding 5% based on membership
m_dis = 0
if m.lower() == "yes":
    m_dis = price * per5
    price -= m_dis
    print(f"Membership discount: {per_5}% = ${m_dis}")
else:
    print(f"Membership discount: {m_dis}")

print(f"Final price per ticket: ${price}")
print(f"Total for {n} tickets: ${price * n}")