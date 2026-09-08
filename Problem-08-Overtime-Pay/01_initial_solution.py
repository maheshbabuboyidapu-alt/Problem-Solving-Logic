rate = int(input("Enter the rate per hour: "))
hours = int(input("Enter worked hours: "))
day = input("Enter day of worked (Weekday/Saturday/Sunday): ").strip().lower()
night_shift = input("Night shift (Yes/No): ").strip().lower()

# Constants
STANDARD_CAP = 8
MAX_OVERTIME_CAP = 4
NIGHT_SHIFT_BONUS = 50

MULTIPLIERS = {
    "weekday": 1.5,
    "saturday": 2.0,
    "sunday": 2.5
}

# 1. Calculate Regular Hours & Pay
regular_hours = min(hours, STANDARD_CAP)
regular_pay = regular_hours * rate
print(f"Regular hours: {regular_hours}")
print(f"Regular pay: {regular_hours} x ${rate} = ${regular_pay}")

# 2. Calculate Overtime Hours
raw_overtime = max(0, hours - STANDARD_CAP)
overtime_hours = min(raw_overtime, MAX_OVERTIME_CAP)

if raw_overtime > 0:
    print(f"Raw overtime hours: {raw_overtime} hours")
    if raw_overtime > MAX_OVERTIME_CAP:
        print(f"Capped overtime: {overtime_hours} hours")
else:
    print("Overtime hours: No")

# 3. Calculate Overtime Pay & Night Bonus
multiplier = MULTIPLIERS.get(day, 1.5)
overtime_hour_rate = rate * multiplier
overtime_pay = overtime_hours * overtime_hour_rate

if overtime_hours > 0:
    print(f"Overtime rate: {multiplier}x = ${overtime_hour_rate}/hr")
    print(f"Overtime pay: {overtime_hours} x ${overtime_hour_rate} = ${overtime_pay}")

night_bonus = 0
if night_shift == "yes" and overtime_hours > 0:
    night_bonus = overtime_hours * NIGHT_SHIFT_BONUS
    print(f"Night bonus: {overtime_hours} x ${NIGHT_SHIFT_BONUS} = ${night_bonus}")
else:
    print("Night bonus: None")

# 4. Total Payment
total_pay = regular_pay + overtime_pay + night_bonus
print(f"Total payment: ${regular_pay} + ${overtime_pay} + ${night_bonus} = ${total_pay}")