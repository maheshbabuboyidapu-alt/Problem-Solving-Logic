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
"""

# ===============================================
# Step 1: Student Score Data
# ===============================================

records = [
    ("Ravi", "Math", 80),
    ("Ravi", "Science", 85),
    ("Ravi", "English", 90),
    ("Priya", "Math", 25),
    ("Priya", "Science", 30),
    ("Priya", "English", 20),
    ("Kumar", "Math", 10),
    ("Kumar", "Science", 15),
    ("Kumar", "English", 12),
]

# ===============================================
# Step 2: Program Constants
# ===============================================

STUDENT_NAME = 0
SUBJECT_NAME = 1
MARKS = 2

# ===============================================
# Step 3: Validate Records
# ===============================================

if not records:
    print("No student records found.")
    exit()

# ===============================================
# Step 4: Calculate Student Averages
# ===============================================

student_totals = {}
student_counts = {}

for record in records:
    student = record[STUDENT_NAME]
    marks = record[MARKS]

    student_totals[student] = student_totals.get(student, 0) + marks
    student_counts[student] = student_counts.get(student, 0) + 1

student_averages = []

for student in student_totals:
    average = student_totals[student] / student_counts[student]
    student_averages.append((student, round(average, 2)))

student_averages.sort(key=lambda item: item[1], reverse=True)

# The first student has the highest average after sorting.
top_student, top_score = student_averages[0]

# ===============================================
# Step 5: Display Student Averages
# ===============================================

print("--- Student Averages ---")

for student, average in student_averages:
    print(f"{student:<8}:{average}")

print(f"\nTop Scorer:{top_student}({top_score})\n")

# ===============================================
# Step 6: Calculate Subject Averages
# ===============================================

subject_totals = {}
subject_counts = {}

for record in records:
    subject = record[SUBJECT_NAME]
    marks = record[MARKS]

    subject_totals[subject] = subject_totals.get(subject, 0) + marks
    subject_counts[subject] = subject_counts.get(subject, 0) + 1

subject_averages = []

for subject in subject_totals:
    average = subject_totals[subject] / subject_counts[subject]
    subject_averages.append((subject, round(average, 2)))

subject_averages.sort(key=lambda item: item[1], reverse=True)

# The last subject has the lowest average after descending sorting.
hardest_subject, lowest_average = subject_averages[-1]

# ===============================================
# Step 7: Display Subject Averages
# ===============================================

print("--- Subject Averages ---")

for subject, average in subject_averages:
    print(f"{subject:<8}:{average}")

print(f"\nHardest Subject:{hardest_subject}({lowest_average})\n")
