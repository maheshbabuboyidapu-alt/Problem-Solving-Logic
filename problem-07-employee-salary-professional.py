"""
Employee Salary & Bonus Calculator

Description:
This program calculates an employee's final take-home salary based on
years of experience, performance rating, attendance percentage, and
applicable tax deductions.

Salary Structure:

Base Salary (by years of experience):
- 0-2 years:   ₹25,000
- 3-5 years:   ₹40,000
- 6-10 years:  ₹60,000
- 11+ years:   ₹90,000

Performance Bonus (percentage of base salary):
- Poor:      0% bonus
- Average:   5% bonus
- Good:      10% bonus
- Excellent: 20% bonus

Attendance Penalty (applied on base + bonus):
- 95-100% attendance: No penalty
- 85-94% attendance:  5% penalty
- 70-84% attendance:  10% penalty
- Below 70%:          20% penalty

Tax Deduction (applied on final amount, before tax):
- Up to ₹30,000:        No tax
- ₹30,001 - ₹60,000:    10% tax
- ₹60,001 - ₹100,000:   20% tax
- Above ₹100,000:       30% tax

Final Salary = Base + Bonus - Penalty - Tax
"""

# ===============================================
# Step 1: Input Collection and Validation
# ===============================================

# Get years of experience
years_of_experience = int(input("Enter the employee's years of experience: "))
if years_of_experience < 0:
    print("Error: Years of experience cannot be negative")
    exit()

# Get performance rating with validation
performance_rating = input("Enter performance rating (Poor/Average/Good/Excellent): ")
valid_ratings = ["poor", "average", "good", "excellent"]
if performance_rating.lower() not in valid_ratings:
    print("Error: Invalid rating! Must be Poor, Average, Good, or Excellent")
    exit()

# Get attendance percentage with validation
attendance_percentage = int(input("Enter employee attendance percentage: "))
if attendance_percentage < 0 or attendance_percentage > 100:
    print("Error: Attendance must be between 0 and 100")
    exit()

# ===============================================
# Step 2: Calculate Base Salary (By Experience Tier)
# ===============================================

if years_of_experience <= 2:
    base_salary = 25000
elif years_of_experience <= 5:
    base_salary = 40000
elif years_of_experience <= 10:
    base_salary = 60000
else:  # 11+ years
    base_salary = 90000

print(f"Base salary: ₹{base_salary:.2f}")

# ===============================================
# Step 3: Apply Performance Bonus
# ===============================================

rating_lower = performance_rating.lower()

if rating_lower == "poor":
    bonus_percentage = 0
elif rating_lower == "average":
    bonus_percentage = 5
elif rating_lower == "good":
    bonus_percentage = 10
else:  # excellent
    bonus_percentage = 20

bonus_amount = base_salary * (bonus_percentage / 100)
print(f"Bonus: {bonus_percentage}% = ₹{bonus_amount:.2f}")

base_salary += bonus_amount
print(f"After bonus: ₹{base_salary:.2f}")

# ===============================================
# Step 4: Apply Attendance Penalty
# ===============================================

if attendance_percentage < 70:
    penalty_percentage = 20
elif attendance_percentage < 85:
    penalty_percentage = 10
elif attendance_percentage < 95:
    penalty_percentage = 5
else:  # 95-100%, guaranteed by earlier validation (0-100 range)
    penalty_percentage = 0

penalty_amount = base_salary * (penalty_percentage / 100)
print(f"Attendance penalty: {penalty_percentage}% = ₹{penalty_amount:.2f}")

base_salary -= penalty_amount
print(f"After penalty: ₹{base_salary:.2f}")

# ===============================================
# Step 5: Calculate Tax (Tiered Based on Final Amount)
# ===============================================

if base_salary <= 30000:
    tax_percentage = 0
elif base_salary <= 60000:
    tax_percentage = 10
elif base_salary <= 100000:
    tax_percentage = 20
else:  # above ₹100,000 — these 4 brackets cover every possible amount
    tax_percentage = 30

tax_amount = base_salary * (tax_percentage / 100)
print(f"Tax: {tax_percentage}% = ₹{tax_amount:.2f}")

# ===============================================
# Step 6: Calculate Final Take-Home Salary
# ===============================================

final_salary = base_salary - tax_amount
print(f"Final salary: ₹{final_salary:.2f}")