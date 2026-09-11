"""
Team Payroll Summary

Description:
This program calculates employee salaries based on regular and overtime
hours, then displays a summary of the team's payroll.

Payroll Structure:
- Up to 40 hours: regular hourly rate
- Hours above 40: 1.5 × hourly rate

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
    {"name": "Ravi", "hours": 45, "rate": 200},
    {"name": "Sita", "hours": 38, "rate": 250},
    {"name": "Arjun", "hours": 50, "rate": 180},
    {"name": "Divya", "hours": 40, "rate": 220},
]

# ===============================================
# Step 2: Program Constants
# ===============================================

STANDARD_HOURS = 40
OVERTIME_MULTIPLIER = 1.5

# ===============================================
# Step 3: Validate Employee Data
# ===============================================

if not employees:
    print("No employees found.")
    exit()

# ===============================================
# Step 4: Initialize Payroll Variables
# ===============================================

total_payroll = 0
employee_count = 0
highest_pay = 0
highest_paid_employee = ""
overtime_employee_count = 0

# ===============================================
# Step 5: Calculate Employee Salaries
# ===============================================

for employee in employees:
    hours_worked = employee["hours"]
    hourly_rate = employee["rate"]

    if hours_worked > STANDARD_HOURS:
        regular_hours = STANDARD_HOURS
        overtime_hours = hours_worked - STANDARD_HOURS
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
        salary = regular_pay + overtime_pay
        overtime_employee_count += 1
    else:
        regular_hours = hours_worked
        regular_pay = regular_hours * hourly_rate
        salary = regular_pay

    print(f'{employee["name"]}: ₹{salary:.2f}')

    # Track highest-paid employee
    if salary > highest_pay:
        highest_pay = salary
        highest_paid_employee = employee["name"]

    total_payroll += salary
    employee_count += 1

# ===============================================
# Step 6: Calculate Average Pay
# ===============================================

average_pay = total_payroll / employee_count

# ===============================================
# Step 7: Display Payroll Summary
# ===============================================

print(f"Total payroll: ₹{total_payroll:.2f}")
print(f"Average pay: ₹{average_pay:.2f}")
print(f"Highest paid: {highest_paid_employee}")
print(f"Employees with overtime: {overtime_employee_count}")
