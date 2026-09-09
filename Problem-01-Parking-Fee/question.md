# Problem 01 — Parking Fee Calculator

## Problem Statement

Build a parking fee calculator based on the number of hours a vehicle is parked.

## Rules

- First 2 hours: fixed ₹30.
- Hours 3–5: ₹20 per additional hour.
- After 5 hours: ₹10 per additional hour.
- If the calculated fee is strictly above ₹200, apply a 10% discount.

## Input

Enter the number of hours parked.

## Example

**Input**
```text
h = 7
```

**Expected Output**
```text
Fee is ₹120.00
```

## Constraints

- Hours must be a positive integer.
- Apply the 10% discount only when the calculated fee is strictly greater than ₹200.

## Test Cases

### Test Case 1 — Minimum fixed fee

**Input**
```text
h = 2
```

**Expected Output**
```text
Fee is ₹30.00
```

### Test Case 2 — Hours in tier 2

**Input**
```text
h = 4
```

**Expected Output**
```text
Fee is ₹70.00
```

### Test Case 3 — Hours in tier 3, no discount

**Input**
```text
h = 7
```

**Expected Output**
```text
Fee is ₹120.00
```

### Test Case 4 — Boundary: calculated fee is below ₹200

**Input**
```text
h = 12
```

**Expected Output**
```text
Fee is ₹160.00
```

**Calculation:** ₹30 + (3 × ₹20) + (7 × ₹10) = ₹160. No discount applies.

### Test Case 5 — Discount applies

**Input**
```text
h = 20
```

**Expected Output**
```text
Fee is ₹216.00
```

**Calculation:** ₹30 + (3 × ₹20) + (15 × ₹10) = ₹240. After 10% discount: ₹216.
