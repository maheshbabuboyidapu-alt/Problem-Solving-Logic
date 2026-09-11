"""
Student Score Tracker

Description:
This program analyzes student marks by calculating average scores for
individual students and subjects.

Summary:
- Student averages in descending order
- Top-scoring student
- Subject averages in descending order
- Subject with the lowest average score
- Passed students with an average score of 40 or above
- Failed students with an average score below 40
"""

# ===============================================
# Step 1: Student Score Data
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

# ===============================================
# Step 2: Program Constants
# ===============================================

STUDENT_NAME = 0
SUBJECT_NAME = 1
MARKS = 2
PASS_AVERAGE_LIMIT = 40

# ===============================================
# Step 3: Prepare Student Records
# ===============================================

student_records = []
record_keys = ("name", "subject", "marks")

for record in records:
    student_records.append(dict(zip(record_keys, record)))

# Check whether student data is available
if len(student_records) == 0:
    print("No student records found.")
    exit()

# ===============================================
# Step 4: Find Unique Students and Subjects
# ===============================================

students = []
subjects = []

for record in student_records:
    student = record["name"]
    subject = record["subject"]

    if student not in students:
        students.append(student)

    if subject not in subjects:
        subjects.append(subject)

# ===============================================
# Step 5: Calculate Student Averages
# ===============================================

student_averages = []
top_student = ""
top_score = 0

for student in students:
    total_marks = 0
    subject_count = 0

    for record in student_records:
        if record["name"] == student:
            total_marks += record["marks"]
            subject_count += 1

    average = round(total_marks / subject_count, 2)
    student_averages.append([student, average])

    if average > top_score:
        top_score = average
        top_student = student

student_averages.sort(key=lambda item: item[1], reverse=True)

# ===============================================
# Step 6: Display Student Averages
# ===============================================

print("--- Student Averages ---")

for student, average in student_averages:
    print(f"{student:<8}:{average}")

print(f"\nTop Scorer:{top_student}({top_score})\n")

# ===============================================
# Step 7: Calculate Subject Averages
# ===============================================

subject_averages = []
hardest_subject = ""
lowest_average = None

for subject in subjects:
    total_marks = 0
    student_count = 0

    for record in student_records:
        if record["subject"] == subject:
            total_marks += record["marks"]
            student_count += 1

    average = round(total_marks / student_count, 2)
    subject_averages.append([subject, average])

    if lowest_average is None or average < lowest_average:
        lowest_average = average
        hardest_subject = subject

subject_averages.sort(key=lambda item: item[1], reverse=True)

# ===============================================
# Step 8: Display Subject Averages
# ===============================================

print("--- Subject Averages ---")

for subject, average in subject_averages:
    print(f"{subject:<8}:{average}")

print(f"\nHardest Subject:{hardest_subject}({lowest_average})\n")

# ===============================================
# Step 9: Categorize Students by Average
# ===============================================

passed_students = []
failed_students = []

for student, average in student_averages:
    if average >= PASS_AVERAGE_LIMIT:
        passed_students.append([student, average])
    else:
        failed_students.append([student, average])

# ===============================================
# Step 10: Display Passed Students
# ===============================================

print(f"--- Passed Students (Average >= {PASS_AVERAGE_LIMIT}) ---")

if not passed_students:
    print("None")
else:
    for student, average in passed_students:
        print(f"{student:<8}:{average}")

# ===============================================
# Step 11: Display Failed Students
# ===============================================

print(f"\n--- Failed Students (Average < {PASS_AVERAGE_LIMIT}) ---")

if not failed_students:
    print("None")
else:
    for student, average in failed_students:
        print(f"{student:<8}:{average}")
