"""
Student Score Tracker

Description:
This program processes student exam records and generates a
summary report containing student and subject-level statistics.

Report Includes:
- Student averages
- Top-scoring student
- Subject averages in descending order
- Subject with the lowest average score
- Students whose average score is below 40
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

STUDENT_NAME = 0
SUBJECT_NAME = 1
MARKS = 2
FAIL_AVERAGE_LIMIT = 40

# ===============================================
# Step 3: Validate Records
# ===============================================

if not records:
    print("No student records found.")
    exit()

# ===============================================
# Step 4: Find Unique Students and Subjects
# ===============================================

student_totals = {}
student_counts = {}

for record in records:
    student = record[STUDENT_NAME]
    marks = record[MARKS]

    student_totals[student] = student_totals.get(student, 0) + marks
    student_counts[student] = student_counts.get(student, 0) + 1

student_averages = []
top_student = ""
top_score = 0

for student in student_totals:
    average = student_totals[student] / student_counts[student]
    student_averages.append((student, round(average, 2)))

student_averages.sort(key=lambda item: item[1], reverse=True)

# The first student has the highest average after sorting.
top_student, top_score = student_averages[0]

# ===============================================
# Step 5: Display Student Averages
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
# Step 7: Calculate Subject Averages
# ===============================================

subject_totals = {}
subject_counts = {}

for record in records:
    subject = record[SUBJECT_NAME]
    marks = record[MARKS]

    subject_totals[subject] = subject_totals.get(subject, 0) + marks
    subject_counts[subject] = subject_counts.get(subject, 0) + 1

subject_averages = []
hardest_subject = ""
lowest_average = None

for subject in subject_totals:
    average = subject_totals[subject] / subject_counts[subject]
    subject_averages.append((subject, round(average, 2)))

subject_averages.sort(key=lambda item: item[1], reverse=True)

# The last subject has the lowest average after descending sorting.
hardest_subject, lowest_average = subject_averages[-1]

# ===============================================
# Step 7: Display Subject Averages
# ===============================================

passed_students = []
failed_students = []

for student in student_averages:

    if student[1] >= PASSMARKS:
        passed_students.append(student)
    else:
        failed_students.append(student)

# ===============================================
# Step 8: Find Failed Students
# ===============================================

failed_students = [
    (student, average)
    for student, average in student_averages
    if average < FAIL_AVERAGE_LIMIT
]

# ===============================================
# Step 9: Display Failed Students
# ===============================================

print("--- Failed Students (Average < 40) ---")

if not failed_students:
    print("None")
else:
    for student in failed_students:
        print(f"{student[0]:<8}:{student[1]}")

print()

