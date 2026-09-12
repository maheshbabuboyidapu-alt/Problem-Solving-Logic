"""
Student Score Tracker

Description:
This program processes student exam records and generates a
summary report containing student and subject-level statistics.

Report Includes:
- Student averages
- Top-scoring student
- Lowest-scoring student
- Subject averages
- Hardest subject
- Easiest subject
- Passed students
- Failed students
"""

# ===============================================
# Step 1: Student Record Data
# ===============================================

records = [
    ("Ravi",  "Math",    80),
    ("Ravi",  "Science", 85),
    ("Ravi",  "English", 90),
    ("Priya", "Math",    25),
    ("Priya", "Science", 30),
    ("Priya", "English", 20),
    ("Kumar", "Math",    10),
    ("Kumar", "Science", 15),
    ("Kumar", "English", 12),
]

PASSMARKS = 40

# ===============================================
# Step 2: Convert Records into Dictionaries
# ===============================================

keys = ("name", "subject", "marks")

student_records = []

for record in records:
    student_records.append(dict(zip(keys, record)))

# ===============================================
# Step 3: Find Unique Students and Subjects
# ===============================================

student_names = []
subjects = []

for record in student_records:

    if record["name"] not in student_names:
        student_names.append(record["name"])

    if record["subject"] not in subjects:
        subjects.append(record["subject"])


def calculate_average(total, count):
    return round(total / count, 2)


# ===============================================
# Step 4: Calculate Student Averages
# ===============================================

student_averages = []

for name in student_names:

    total = 0
    count = 0

    for record in student_records:

        if name == record["name"]:
            total += record["marks"]
            count += 1

    average = calculate_average(total, count)
    student_averages.append([name, average])

student_averages = sorted(
    student_averages,
    key=lambda student: student[1],
    reverse=True
)

# ===============================================
# Step 5: Display Student Results
# ===============================================

print("\n========== SUMMARY REPORT OF STUDENT & SUBJECT MARKS ==========\n")

print("--- Student Averages ---")

for student in student_averages:
    print(f"{student[0]:<8}:{student[1]}")

top_student = student_averages[0]
low_student = student_averages[-1]

print(f"\nTop Scorer:{top_student[0]}({top_student[1]})")
print(f"Low Scorer:{low_student[0]}({low_student[1]})")


# ===============================================
# Step 6: Calculate Subject Averages
# ===============================================

print("\n--- Subject Averages ---")

subject_averages = []

for subject in subjects:

    total = 0
    count = 0

    for record in student_records:

        if subject == record["subject"]:
            total += record["marks"]
            count += 1

    average = calculate_average(total, count)
    subject_averages.append([subject, average])

subject_averages = sorted(
    subject_averages,
    key=lambda subject: subject[1],
    reverse=True
)

# ===============================================
# Step 7: Display Subject Results
# ===============================================

for subject in subject_averages:
    print(f"{subject[0]:<8}:{subject[1]}")

hardest_subject = subject_averages[-1]
easiest_subject = subject_averages[0]

print(
    f"\nHardest Subject:{hardest_subject[0]}"
    f"({hardest_subject[1]})"
)

print(
    f"Easiest Subject:{easiest_subject[0]}"
    f"({easiest_subject[1]})"
)


# ===============================================
# Step 8: Separate Passed and Failed Students
# ===============================================

passed_students = []
failed_students = []

for student in student_averages:

    if student[1] >= PASSMARKS:
        passed_students.append(student)
    else:
        failed_students.append(student)

# ===============================================
# Step 9: Display Passed Students
# ===============================================

print(f"\n--- Passed Students (Average >= {PASSMARKS}) ---")

if not passed_students:
    print("None")
else:
    for student in passed_students:
        print(f"{student[0]:<8}:{student[1]}")


# ===============================================
# Step 10: Display Failed Students
# ===============================================

print(f"\n--- Failed Students (Average < {PASSMARKS}) ---")

failed_students = sorted(
    failed_students,
    key=lambda student: student[1]
)

if not failed_students:
    print("None")
else:
    for student in failed_students:
        print(f"{student[0]:<8}:{student[1]}")

print()

