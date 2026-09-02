
"""
Team Payroll Summary

Description:
This program calculates the total payroll for a team of employees based
on their working hours and hourly pay rate.

Payroll Structure:

Regular Pay:
- Up to 40 hours: regular hourly rate

Overtime Pay:
- Hours above 40: 1.5 times the regular hourly rate

Final Pay:
- Regular Pay + Overtime Pay

Payroll Summary:
- Individual employee salary
- Total payroll
- Average employee pay
- Highest-paid employee
- Number of employees who worked overtime
"""

# ===============================================
# Step 1: Employee Data
# ===============================================

employees = [
    
]

# ===============================================
# Step 2: Initialize Payroll Variables
# ===============================================

total_payroll = 0
employee_count = 0
highest_pay = 0
highest_paid_employee = ""
overtime_employee_count = 0

# Check whether employee data is available
if len(employees) == 0:
    print("No employees found.")
    exit()

# ===============================================
# Step 3: Calculate Employee Salary
# ===============================================

for employee in employees:
    hours_worked = employee["hours"]
    hourly_rate = employee["rate"]

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40

        overtime_pay = overtime_hours * (hourly_rate * 1.5)
        regular_pay = regular_hours * hourly_rate
        salary = regular_pay + overtime_pay

        overtime_employee_count += 1

    else:
        regular_hours = hours_worked
        regular_pay = regular_hours * hourly_rate
        salary = regular_pay

    print(f'{employee["name"]}: ₹{salary:.2f}')

    # ===========================================
    # Track Highest Paid Employee
    # ===========================================

    if salary > highest_pay:
        highest_pay = salary
        highest_paid_employee = employee["name"]

    total_payroll += salary
    employee_count += 1

# ===============================================
# Step 4: Calculate Average Pay
# ===============================================

average_pay = total_payroll / employee_count

# ===============================================
# Step 5: Display Payroll Summary
# ===============================================

print(f"Total payroll: ₹{total_payroll:.2f}")
print(f"Average pay: ₹{average_pay:.2f}")
print(f"Highest paid: {highest_paid_employee}")
print(f"Employees with overtime: {overtime_employee_count}")

