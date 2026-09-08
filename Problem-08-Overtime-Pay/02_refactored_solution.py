"""
Employee Overtime & Night Shift Pay Calculator

Description:
This program calculates an employee's total daily earnings based on
their hourly wage, total hours worked, workday category, and
night shift eligibility.

Payment Structure:

Regular Pay:
- The first 8 working hours are paid at the standard hourly rate.

Overtime Pay:
- Any hours worked beyond 8 hours are considered overtime.
- A maximum of 4 overtime hours are eligible for overtime payment.

Overtime Multipliers:
- Weekday:  1.5 × hourly rate
- Saturday: 2.0 × hourly rate
- Sunday:   2.5 × hourly rate

Night Shift Bonus:
- Employees working a night shift receive an additional
  $50 bonus for each eligible overtime hour.

Final Payment = Regular Pay + Overtime Pay + Night Shift Bonus
"""

# ===============================================
# Step 1: Input Collection and Validation
# ===============================================

# Get hourly wage
hourly_rate = float(input("Enter employee hourly rate: "))
if hourly_rate < 0:
    print("Error: Hourly rate cannot be negative.")
    exit()

# Get total worked hours
worked_hours = float(input("Enter total worked hours: "))
if worked_hours < 0:
    print("Error: Worked hours cannot be negative.")
    exit()

# Get workday
work_day = input("Enter work day (Weekday/Saturday/Sunday): ").strip().lower()
valid_days = ["weekday", "saturday", "sunday"]

if work_day not in valid_days:
    print("Error: Invalid work day.")
    exit()

# Get night shift status
night_shift = input("Night shift (Yes/No): ").strip().lower()

if night_shift not in ["yes", "no"]:
    print("Error: Night shift must be Yes or No.")
    exit()

# ===============================================
# Step 2: Program Constants
# ===============================================

STANDARD_HOURS = 8
MAX_OVERTIME = 4
NIGHT_SHIFT_BONUS = 50

OVERTIME_MULTIPLIERS = {
    "weekday": 1.5,
    "saturday": 2.0,
    "sunday": 2.5
}

print("\n========== PAYMENT SUMMARY ==========")

# ===============================================
# Step 3: Calculate Regular Pay
# ===============================================

regular_hours = min(worked_hours, STANDARD_HOURS)
regular_pay = regular_hours * hourly_rate

print(f"Regular hours : {regular_hours}")
print(f"Regular pay   : {regular_hours} × ${hourly_rate:.2f} = ${regular_pay:.2f}")

# ===============================================
# Step 4: Calculate Overtime Hours
# ===============================================

actual_overtime = max(0, worked_hours - STANDARD_HOURS)
overtime_hours = min(actual_overtime, MAX_OVERTIME)

if actual_overtime == 0:
    print("Overtime      : None")
else:
    print(f"Actual overtime hours : {actual_overtime}")

    if actual_overtime > MAX_OVERTIME:
        print(f"Eligible overtime     : {overtime_hours} (Maximum limit applied)")
    else:
        print(f"Eligible overtime     : {overtime_hours}")

# ===============================================
# Step 5: Calculate Overtime Pay
# ===============================================

multiplier = OVERTIME_MULTIPLIERS[work_day]
overtime_rate = hourly_rate * multiplier
overtime_pay = overtime_hours * overtime_rate

if overtime_hours > 0:
    print(f"Overtime rate : {multiplier} × ${hourly_rate:.2f} = ${overtime_rate:.2f}/hour")
    print(f"Overtime pay  : {overtime_hours} × ${overtime_rate:.2f} = ${overtime_pay:.2f}")
else:
    print("Overtime pay  : $0.00")

# ===============================================
# Step 6: Calculate Night Shift Bonus
# ===============================================

if night_shift == "yes":
    night_bonus = overtime_hours * NIGHT_SHIFT_BONUS
else:
    night_bonus = 0

if night_bonus > 0:
    print(f"Night bonus   : {overtime_hours} × ${NIGHT_SHIFT_BONUS:.2f} = ${night_bonus:.2f}")
elif night_shift == "yes":
    print("Night bonus   : None (No eligible overtime)")
else:
    print("Night bonus   : None")

# ===============================================
# Step 7: Calculate Final Payment
# ===============================================

total_payment = regular_pay + overtime_pay + night_bonus

print("--------------------------------------------")
print(f"Regular Pay      : ${regular_pay:.2f}")
print(f"Overtime Pay     : ${overtime_pay:.2f}")
print(f"Night Shift Bonus: ${night_bonus:.2f}")
print("--------------------------------------------")
print(f"Total Payment    : ${total_payment:.2f}")