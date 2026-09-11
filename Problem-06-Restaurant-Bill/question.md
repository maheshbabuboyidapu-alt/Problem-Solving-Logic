# Problem 06 — Restaurant Bill Calculator

## Problem Statement

Calculate the final restaurant bill for a customer by applying discounts, tax, and tip in the required order.

## Rules

### 1. Food amount

Food amount = quantity × price per item.

### 2. Bulk discount

Applied to the food amount:

- Food amount strictly above ₹5,000: 5% discount.
- Otherwise: no bulk discount.

### 3. Member discount

Applied after the bulk discount:

- Regular member: 10% discount.
- Non-member: no discount.

### 4. Tax

Applied to the subtotal after all discounts:

- Below ₹500: 5% tax.
- ₹500–₹2,000: 12% tax.
- Above ₹2,000: 18% tax.

### 5. Tip

Calculated on the subtotal after discounts and before tax:

- Custom tip: fixed amount entered by the user.
- Percentage tip: exactly 10%, 15%, or 20% of the subtotal.
- No tip: ₹0.

Final bill = subtotal + tax + tip.

## Input

Enter:

1. Food item name.
2. Quantity.
3. Price per item.
4. Tip choice: `1` custom tip, `2` percentage tip, or `3` no tip.
5. For choice `1`, enter the fixed custom tip amount.
6. For choice `2`, enter 10, 15, or 20 as the percentage.
7. Membership status: regular or non-member.

## Example

**Input**
```text
item = Biryani
qty = 3
price = 400
tip choice = 2
percentage = 15
membership = regular
```

**Expected Output**
```text
Food amount: 3 × ₹400.00 = ₹1200.00
Bulk discount: None
Subtotal after bulk discount: ₹1200.00
Member discount: 10% = −₹120.00
Final subtotal: ₹1080.00
Tax: 12% of ₹1080.00 = ₹129.60
Tip: 15% of ₹1080.00 = ₹162.00
Final bill: ₹1371.60
```

## Constraints

- Tip percentage must be exactly 10, 15, or 20 when percentage tipping is selected.
- Apply discounts before calculating tax.
- Tip is calculated on the subtotal after discounts but before tax.
- Bulk discount applies only when food amount is strictly greater than ₹5,000.

## Test Cases

### Test Case 1 — No bulk discount, member, percentage tip

**Input**
```text
item = Biryani
qty = 3
price = 400
tip = 2 (15%)
membership = regular
```

**Expected Output**
```text
Food amount: ₹1200.00
Bulk discount: None
Member discount: 10% = ₹120.00
Subtotal: ₹1080.00
Tax: 12% = ₹129.60
Tip: 15% = ₹162.00
Final bill: ₹1371.60
```

### Test Case 2 — Bulk discount, non-member, no tip

**Input**
```text
item = Thali
qty = 20
price = 300
tip = 3 (no tip)
membership = non-member
```

**Expected Output**
```text
Food amount: ₹6000.00
Bulk discount: 5% = ₹300.00
After discount: ₹5700.00
Member discount: None
Tax: 18% = ₹1026.00
Tip: ₹0.00
Final bill: ₹6726.00
```

### Test Case 3 — Low tax tier with custom tip

**Input**
```text
item = Tea
qty = 2
price = 50
tip = 1 (custom ₹20)
membership = non-member
```

**Expected Output**
```text
Food amount: ₹100.00
Bulk discount: None
Member discount: None
Tax: 5% = ₹5.00
Tip: ₹20.00
Final bill: ₹125.00
```

### Test Case 4 — Boundary: food amount exactly ₹5,000

**Input**
```text
item = Meal
qty = 10
price = 500
tip = 3 (no tip)
membership = non-member
```

**Expected Output**
```text
Food amount: ₹5000.00
Bulk discount: None
Tax: 18% = ₹900.00
Final bill: ₹5900.00
```

The bulk discount does not apply because the rule is strictly greater than ₹5,000.

### Test Case 5 — Invalid tip percentage

**Input**
```text
tip choice = 2
percentage = 25
```

**Expected Output**
```text
Invalid percentage!
```
