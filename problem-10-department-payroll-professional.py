
"""
Department Payroll Breakdown

Description:
This program calculates the payroll of employees and generates a
department-wise payroll breakdown based on their working hours
and hourly pay rate.

Payroll Structure:

Regular Pay:
- Up to 40 hours: regular hourly rate

Overtime Pay:
- Hours above 40: 1.5 times the regular hourly rate

Final Pay:
- Regular Pay + Overtime Pay

Department Payroll Summary:
- Individual employee salary
- Total department payroll
- Highest-paid employee in each department
- Lowest-paid employee in each department
"""

# ===============================================
# Step 1: Employee Data
# ===============================================

employees = [
    {"name": "Ravi",  "department": "Engineering", "hours": 45, "rate": 200},
    {"name": "Sita",  "department": "Sales",       "hours": 38, "rate": 250},
    {"name": "Arjun", "department": "Engineering", "hours": 50, "rate": 180},
    {"name": "Divya", "department": "Sales",       "hours": 40, "rate": 220},
]

# ===============================================
# Step 2: Find Unique Departments
# ===============================================

departments = []

for employee in employees:
    department = employee["department"]

    if department not in departments:
        departments.append(department)

# Check whether employee data is available
if len(employees) == 0:
    print("No employees found.")
    exit()

# ===============================================
# Step 3: Process Each Department
# ===============================================

for department in departments:

    total_payroll = 0
    highest_pay = 0
    highest_paid_employee = ""
    lowest_pay = None
    lowest_paid_employee = ""

    print(f"Department: {department}")

    # ===========================================
    # Step 4: Calculate Employee Salary
    # ===========================================

    for employee in employees:

        if employee["department"] == department:

            hours_worked = employee["hours"]
            hourly_rate = employee["rate"]

            if hours_worked > 40:
                overtime_hours = hours_worked - 40
                regular_hours = 40

                overtime_pay = overtime_hours * (hourly_rate * 1.5)
                regular_pay = regular_hours * hourly_rate
                salary = regular_pay + overtime_pay

            else:
                regular_hours = hours_worked
                regular_pay = regular_hours * hourly_rate
                salary = regular_pay

            print(f'   - {employee["name"]}: ₹{salary:.2f}')

            total_payroll += salary

            # ===================================
            # Track Highest Paid Employee
            # ===================================

            if salary > highest_pay:
                highest_pay = salary
                highest_paid_employee = employee["name"]

            # ===================================
            # Track Lowest Paid Employee
            # ===================================

            if lowest_pay is None or salary < lowest_pay:
                lowest_pay = salary
                lowest_paid_employee = employee["name"]

    # ===========================================
    # Step 5: Display Department Summary
    # ===========================================

    print(f"Total of {department} department: ₹{total_payroll:.2f}")
    print(
        f"Highest paid person in the {department} department: "
        f"{highest_paid_employee} (₹{highest_pay:.2f})"
    )
    print(
        f"Lowest paid person in the {department} department: "
        f"{lowest_paid_employee} (₹{lowest_pay:.2f})"
    )
    print()
