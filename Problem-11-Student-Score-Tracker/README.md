# Problem 11 — Student Score Tracker

## Problem

Process student exam records and generate a summary report containing:

- Student averages sorted from highest to lowest
- Top-scoring student
- Subject averages sorted from highest to lowest
- Hardest subject based on the lowest subject average
- Passed students with an average of 40 or above
- Failed students with an average below 40

Each record contains a student's name, subject, and score.

## Real-World Scenario

This models a simple school score-reporting system where individual exam records must be processed to produce useful student and subject-level statistics.

## Concepts Applied

- Lists
- Tuples
- Dictionaries
- `for` loops
- Nested iteration
- Index-based tuple access
- Conditional statements
- Arithmetic calculations
- Accumulator variables
- Average calculation
- Sorting with `sort()` and `lambda`
- Highest/lowest value tracking
- Filtering records based on a condition
- Constants for tuple positions and pass/fail threshold

## My Approach

I first identified the information stored in each tuple and used constants to make the tuple positions easier to understand.

Then I processed the records to calculate each student's total marks and number of subjects. From these values, I calculated the student averages and sorted them from highest to lowest to identify the top scorer.

I applied the same processing idea to calculate subject averages and identify the hardest subject.

Finally, I used the calculated student averages to separate students into passed and failed groups. A student is considered passed when their average is 40 or above and failed when their average is below 40.

The refactored solution keeps the same overall problem-solving approach while improving naming, organization, readability, and structure.

## What I Learned

- How to process multiple records containing related information.
- How to calculate averages using totals and counts.
- How to reuse calculated results for additional requirements such as pass/fail classification.
- How sorting can make it easier to identify highest and lowest results.
- How a constant can make tuple indexes and business rules easier to understand.
- How the same data can be analyzed from different perspectives, such as by student and by subject.

## Rules

- A student fails only when their average is **below 40**.
- An average of exactly **40** is considered a pass.
- All averages are rounded to **2 decimal places**.
- Students are displayed in descending order of average.
- Subjects are displayed in descending order of average.

## Test Cases

### Test Case 1 — Normal Case

Uses the given data and produces no failed students.

Expected highlights:

- Top scorer: **Anjali (91.67)**
- Hardest subject: **English (59.33)**
- Failed students: **None**

### Test Case 2 — One Student Fails

Kumar has marks of 20, 15, and 10.

Expected highlights:

- Top scorer: **Anjali (91.67)**
- Failed student: **Kumar (15.0)**

### Test Case 3 — Equal Averages

All students and subjects have an average of 70.

Expected highlights:

- Student averages: **70.0**
- Subject averages: **70.0**
- Failed students: **None**

The order of equal averages can be any consistent order.

### Test Case 4 — Boundary at 40

Meena has an average of exactly 40.

Expected highlights:

- Meena average: **40.0**
- Failed students: **None**

This verifies that the failure condition is strictly below 40.

### Test Case 5 — Multiple Students Fail

Priya and Kumar both have averages below 40.

Expected highlights:

- Top scorer: **Ravi (85.0)**
- Failed students: **Priya (25.0), Kumar (12.33)**

## Files

- `question.md` — Problem statement, constraints, expected output, and test cases
- `01_initial_solution.py` — My initial problem-solving implementation
- `02_refactored_solution.py` — Refactored version of the same approach
