# Problem 09 — Team Payroll Summary

## Problem Statement

Process the payroll for a team of employees and generate a summary report.

## Salary Rules

- Up to 40 hours: paid at the normal hourly rate.
- Hours beyond 40: paid at 1.5× the normal hourly rate.

## Report Requirements

Calculate and report:

- Individual salary for each employee.
- Total team payroll.
- Average pay across the team.
- Name of the highest-paid employee.
- Number of employees who worked overtime.

## Input/Data

```python
employees = [
    {"name": "Ravi",  "hours": 45, "rate": 200},
    {"name": "Sita",  "hours": 38, "rate": 250},
    {"name": "Arjun", "hours": 50, "rate": 180},
    {"name": "Divya", "hours": 40, "rate": 220},
]
```

## Expected Output

```text
Ravi  : ₹9500.00
Sita  : ₹9500.00
Arjun : ₹9900.00
Divya : ₹8800.00
Total payroll           : ₹37700.00
Average pay             : ₹9425.00
Highest paid            : Arjun
Employees with overtime : 2
```

## Constraints

- Overtime rate is exactly 1.5× the normal hourly rate.
- Only hours beyond 40 count as overtime.
- Handle an empty employee list safely.

## Test Cases

### Test Case 1 — Given data

Use the same employee data as the example.

**Expected:**
```text
Ravi  : ₹9500.00
Sita  : ₹9500.00
Arjun : ₹9900.00
Divya : ₹8800.00
Total: ₹37700.00
Average: ₹9425.00
Highest paid: Arjun
OT employees: 2
```

### Test Case 2 — Everyone works exactly 40 hours

```python
employees = [
    {"name": "Kiran", "hours": 40, "rate": 300},
    {"name": "Meena", "hours": 40, "rate": 250},
]
```

**Expected:**
```text
Kiran : ₹12000.00
Meena : ₹10000.00
Total: ₹22000.00
Average: ₹11000.00
Highest paid: Kiran
OT employees: 0
```

### Test Case 3 — Everyone works overtime

```python
employees = [
    {"name": "Asha", "hours": 48, "rate": 200},
    {"name": "Vijay", "hours": 44, "rate": 300},
]
```

**Expected:**
```text
Asha  : ₹10400.00
Vijay : ₹13800.00
Total: ₹24200.00
Average: ₹12100.00
Highest paid: Vijay
OT employees: 2
```

### Test Case 4 — Boundary: exactly 40 hours

```python
employees = [
    {"name": "Raj", "hours": 40, "rate": 500},
]
```

**Expected:**
```text
Raj: ₹20000.00
OT employees: 0
```

### Test Case 5 — Empty employee list

```python
employees = []
```

**Expected:**
```text
No employees found.
```
