employees = [
    {"name": "Ravi",  "hours": 45, "rate": 200},
    {"name": "Sita",  "hours": 38, "rate": 250},
    {"name": "Arjun", "hours": 50, "rate": 180},
    {"name": "Divya", "hours": 40, "rate": 220},
]

total_payroll=0
n_of_elements=0
highest_pay=0
n_of_ot_mem=0
for emp in employees:
    if emp["hours"] > 40:
        ot_h=emp["hours"]-40
        rt_h=40
        ot_pay=ot_h*(emp["rate"]*1.5)
        rt_pay=rt_h*emp["rate"]
        salary=ot_pay+rt_pay
        n_of_ot_mem+=1
    else:
        rt_h=emp["hours"]
        rt_pay=rt_h*emp["rate"]
        salary=rt_pay
    if salary > highest_pay :
        highest_pay=salary
        name_of_highest=emp["name"]
    print(f'{emp["name"]}: ₹{salary:.2f}')
    total_payroll+=salary
    n_of_elements+=1
average=total_payroll/n_of_elements
print(f"Total payroll: ₹{total_payroll:.2f}")
print(f"Average pay: ₹{average:.2f}")
print(f"Highest paid: {name_of_highest}")
print(f"Employees with overtime: {n_of_ot_mem}")

