# Problem 11 — Student Score Tracker

## Problem Statement

A school stores exam records for multiple students across multiple subjects. Each record is represented as:

```text
(student, subject, score)
```

Build a program that processes the records and generates a student-wise and subject-wise summary.

## Input Data

```python
records = [
    ("Ravi",   "Math",    78),
    ("Anjali", "Math",    92),
    ("Ravi",   "Science", 65),
    ("Priya",  "Math",    55),
    ("Anjali", "Science", 88),
    ("Priya",  "Science", 40),
    ("Ravi",   "English", 50),
    ("Anjali", "English", 95),
    ("Priya",  "English", 33),
]
```

## Required Output

Calculate and report:

1. The average score for every student.
2. The top-scoring student and their average.
3. The average score for every subject.
4. The hardest subject, meaning the subject with the lowest average.
5. Students whose average score is strictly below 40.

## Expected Output

```text
--- Student Averages ---
Anjali  : 91.67
Ravi    : 64.33
Priya   : 42.67

Top Scorer: Anjali (91.67)

--- Subject Averages ---
Math    : 75.0
Science : 64.33
English : 59.33

Hardest Subject: English (59.33)

--- Failed Students (Average < 40) ---
None
```

## Constraints

- A student fails only when their average is strictly less than 40.
- Round averages to 2 decimal places for calculations/output where decimal formatting is shown.
- Students must be sorted by average from highest to lowest.
- Subjects must be sorted by average from highest to lowest.
- For equal averages, any consistent tie order is acceptable.

## Test Cases

### Test Case 1 — Normal case

Use the given `records` data.

**Expected key results:**
```text
Top Scorer: Anjali (91.67)
Hardest Subject: English (59.33)
Failed Students: None
```

### Test Case 2 — One student fails

```python
records = [
    ("Ravi",   "Math",    78),
    ("Anjali", "Math",    92),
    ("Kumar",  "Math",    20),
    ("Ravi",   "Science", 65),
    ("Anjali", "Science", 88),
    ("Kumar",  "Science", 15),
    ("Ravi",   "English", 50),
    ("Anjali", "English", 95),
    ("Kumar",  "English", 10),
]
```

**Expected key results:**
```text
Top Scorer: Anjali (91.67)
Failed Students:
Kumar : 15.00
```

### Test Case 3 — Equal student averages

Use records that give every student an average of 70, such as:

```python
records = [
    ("A", "Math", 70),
    ("B", "Math", 70),
    ("C", "Math", 70),
]
```

**Expected key results:**
```text
All student averages: 70.00
```

Any consistent order among students with equal averages is acceptable.

### Test Case 4 — Boundary: average exactly 40 does not fail

```python
records = [
    ("Ravi", "Math", 40),
    ("Ravi", "Science", 40),
    ("Anjali", "Math", 80),
    ("Anjali", "Science", 80),
]
```

**Expected key results:**
```text
Ravi average: 40.00
Ravi is not a failed student.
```

### Test Case 5 — Multiple failing students

```python
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
```

**Expected key results:**
```text
Ravi average: 85.00
Priya average: 25.00
Kumar average: 12.33

Failed Students:
Priya : 25.00
Kumar : 12.33
```
