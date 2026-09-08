<<<<<<< HEAD
# Problem-Solving-Logic

A record of my programming problem-solving journey in Python.

## My Learning Approach

I learn one new programming concept first. Then I test my understanding by solving multiple new, real-world problems using the concepts I have learned.

My goal is not to collect problem numbers. My goal is to improve my reasoning, problem-solving ability, code quality, and understanding of how programming can be used to model real-world situations.

### Learning Cycle

```text
Learn a concept
      ↓
Solve a new real-world problem
      ↓
Test my understanding
      ↓
Build another problem
      ↓
Improve my solution
      ↓
Document what I learned
```

## Progression

### Foundation — Problems 01–08

I started with Python fundamentals and focused on translating real-world rules into program logic using conditional statements, calculations, input handling, and validation.

The scenarios include parking, banking, movie tickets, e-commerce, library fines, restaurant billing, employee salary, and overtime payment.

### Applying New Concepts — Problems 09–10

After learning data-oriented Python concepts such as lists and dictionaries, I began applying them to problems involving collections of employees and payroll calculations.

I also started using reusable functions where they helped organize repeated calculations.

The purpose of this stage is to show how my solutions evolve as I learn new concepts.

## What This Repository Shows

- I translate business-style requirements into program logic.
- I practice input validation and edge-case handling.
- I work with real-world rules such as discounts, salary calculations, taxes, overtime, and payroll.
- I compare an initial solution with an improved/refactored solution where available.
- I document what I learned from each problem and how my approach changes over time.
=======
Problem Solving & Logic

A collection of programming problems focused on developing problem-solving ability, logical thinking, and Python fundamentals through progressively more realistic problems.

This repository documents my learning journey from basic conditional logic toward working with loops, collections, aggregation, grouping, and reusable logic.

The goal is to build a strong programming foundation before moving deeper into Data Structures & Algorithms and larger software projects.

---

Learning Philosophy

I follow a simple approach:

«First solve the problem with my current capability. Then learn a new concept and use that new capability in the next problems.»

I intentionally do not learn every Python feature before solving problems.

For the early problems, I used only the concepts I had already learned. For example, I did not immediately use functions or advanced data structures just to make the code look more professional.
>>>>>>> 75fd8ac133a1d0f948b12b3e30e9ee865a9018fb

Instead, I wanted to first understand:

- How to break a problem into logical steps
- How conditions affect the result
- How to translate business rules into code
- How to handle different cases
- How to test my own logic

As the problems became more complex, I began introducing new concepts such as lists, dictionaries, sets, loops, aggregation, and functions.

Therefore, the code in this repository is intentionally a record of my progression rather than a collection of solutions written with every available Python feature.

---

Problems

1. Parking Fee Calculator

Concepts: Tiered pricing, conditional logic, input validation

Introduces basic decision-making by calculating parking fees through multiple pricing tiers and applying a discount when the final fee crosses a threshold.

---

2. Bank Interest Calculator

Concepts: Interest slabs, multi-tier calculations, conditional statements

Introduces multiple balance ranges with different interest rates, bonuses, and deductions.

---

3. Movie Theater Ticket Pricing

Concepts: Age-based pricing, time-based adjustments, discounts, validation, decision making

Combines several independent rules such as customer age, show timing, number of tickets, group discounts, and membership discounts.

This is a step toward handling multiple interacting business conditions.

---

4. E-Commerce Discount & Shipping Calculator

Concepts: Stacked discounts, shipping calculations, coupon rules, validation, conditional logic

Introduces sequential business rules where one calculation affects the next calculation.

The problem requires understanding the order in which rules must be applied.

---

5. Library Fine Calculator

Concepts: Tiered calculations, membership discounts, multipliers, validation, error handling

Introduces more layered calculations involving overdue periods, book types, membership categories, and a maximum fine limit.

---

6. Restaurant Bill Calculator

Concepts: Taxes, discounts, tips, multiple calculation stages, validation

Combines food pricing, quantity, discounts, membership rules, taxation, and multiple tip options.

The main challenge is managing a multi-stage calculation pipeline where each stage affects the final bill.

---

7. Employee Salary & Bonus Calculator

Concepts: Salary slabs, performance bonus, attendance penalty, tax calculation, conditional logic

Combines several independent employee rules into one final salary calculation.

This increases the complexity of translating real-world business requirements into executable logic.

---

8. Employee Overtime & Night Shift Pay Calculator

Concepts: Regular pay, overtime, multipliers, maximum overtime limits, workday rules, night-shift bonus, validation

Introduces more complex payment rules where working hours, day category, overtime limits, overtime multipliers, and night-shift conditions interact with one another.

This problem further develops the ability to manage multiple dependent conditions.

---

9. Team Payroll Summary

Concepts: Loops, dictionaries, aggregation, overtime calculation, minimum/maximum tracking, averages

This is an important transition from processing one set of inputs to processing a collection of employees.

The program:

- Iterates through employee dictionaries
- Calculates individual salaries
- Calculates total team payroll
- Calculates average pay
- Finds the highest-paid employee
- Counts employees who worked overtime

The main progression here is:

Individual calculation → repeated processing → aggregation

---

10. Department Payroll Breakdown

Concepts: Lists, sets, dictionaries, loops, nested loops, unique-value detection, grouping, aggregation, minimum/maximum tracking, functions

This problem extends the previous payroll problem into a more complex department-level payroll system.

Instead of calculating statistics for the entire team, employees must first be grouped logically by department.

The program:

- Stores employee information using dictionaries
- Identifies unique departments
- Uses a "set" to track departments that have already been encountered
- Uses a "list" to maintain the discovered department collection
- Processes each department separately
- Iterates through employees using nested loops
- Calculates individual employee salary including overtime
- Calculates total payroll for each department
- Finds the highest-paid employee in each department
- Finds the lowest-paid employee in each department

The draft version also introduces a reusable function for salary calculation, marking another step in my progression toward code abstraction and reuse.

Progression from Problem 9 to Problem 10

The difference is intentional:

Problem 9

Employees
   ↓
Calculate each employee
   ↓
Team-wide aggregation

Problem 10

Employees
   ↓
Identify unique departments
   ↓
Process each department
   ↓
Process employees inside each department
   ↓
Department-level aggregation

This represents a move from simple collection processing to grouped data processing and nested problem solving.

---

What These Problems Practice

Programming Fundamentals

- Variables and expressions
- Input and output
- Conditional statements
- Validation
- Mathematical calculations

Problem-Solving Skills

- Breaking requirements into smaller rules
- Translating business requirements into code
- Managing multiple conditions
- Designing multi-step calculations
- Handling edge cases
- Testing different scenarios

Data Handling

- Lists
- Dictionaries
- Sets
- Iteration
- Nested iteration
- Unique-value detection
- Aggregation
- Minimum/maximum tracking
- Averages

Code Development

- Readable variable naming
- Constants
- Comments and documentation
- Gradual code organization
- Introduction of reusable functions as my knowledge grows

---

My Development Approach

For each problem, I try to follow this process:

1. Understand the requirements.
2. Identify inputs, outputs, and business rules.
3. Break the problem into smaller logical steps.
4. Implement the solution using the concepts I currently know.
5. Test different cases and edge cases.
6. Learn new concepts when the next problem requires them.
7. Apply those new concepts to increasingly complex problems.

This means the repository shows growth over time, rather than pretending that every solution was written with advanced techniques from the beginning.

---

Repository Structure

Problem-Solving-Logic/
│
<<<<<<< HEAD
├── Problem-01-Parking-Fee/
├── Problem-02-Bank-Interest/
├── Problem-03-Movie-Theater/
├── Problem-04-E-commerce/
├── Problem-05-Library-Fine/
├── Problem-06-Restaurant-Bill/
├── Problem-07-Employee-Salary/
├── Problem-08-Overtime-Pay/
├── Problem-09-Team-Payroll/
└── Problem-10-Department-Payroll/
```

Each problem contains the solution(s) and a README describing the problem, the concepts applied, my approach, and what I learned.

## Long-Term Goal

I will continue this repository while I am developing my problem-solving foundation. Later, when I move into dedicated DSA practice, this repository will naturally become a record of the stage where I built my programming logic through real-world problems.
=======
├── problem-01-parking-draft.py
├── problem-01-parking-professional.py
│
├── problem-02-bank-interest-draft.py
├── problem-02-bank-interest-professional.py
│
├── problem-03-movie-theater-draft.py
├── problem-03-movie-theater-professional.py
│
├── problem-04-ecommerce-discount-draft.py
├── problem-04-ecommerce-discount-professional.py
│
├── problem-05-library-fines-draft.py
├── problem-05-library-fines-professional.py
│
├── problem-06-restaurant-bill-draft.py
├── problem-06-restaurant-bill-professional.py
│
├── problem-07-employee-salary-draft.py
├── problem-07-employee-salary-professional.py
│
├── problem-08-employee-overtime-payment-calculator-draft.py
├── problem-08-employee-overtime-payment-calculator-professional.py
│
├── problem-09-team-pay-roll-summary-draft.py
├── problem-09-team-pay-roll-summary-professional.py
│
├── problem-10-department-payroll-draft.py
├── problem-10-department-payroll-professional.py
│
└── README.md

---

Current Focus

Problem Solving & Python Fundamentals

The problems are gradually moving from simple conditional logic toward working with collections, grouped data, reusable logic, and more complex problem structures.

The next phase will build on this foundation with Data Structures & Algorithms and larger programming projects.

---

Purpose

This repository is not intended to show that I already know everything about Python.

It is intended to show how I learn, how I solve problems independently, and how my capabilities develop as the problems become more complex.

I want to understand the logic first and then learn the better tools and techniques needed to solve harder problems.

---

«First build the logic. Then build the capability. Then build bigger things.»
>>>>>>> 75fd8ac133a1d0f948b12b3e30e9ee865a9018fb
