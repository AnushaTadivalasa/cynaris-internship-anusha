-- database: :memory:
-- ============================================
-- WEEK 1 - DAY 4
-- SQL Subqueries & CTEs
-- ============================================

-- 1. Create Employees Table

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    employee_id INTEGER,
    employee_name TEXT,
    department TEXT,
    job_role TEXT,
    region TEXT,
    experience_years INTEGER,
    salary REAL,
    sales_amount REAL,
    age INTEGER,
    performance_score REAL
);


-- 2. Insert 20 Employee Records

INSERT INTO employees VALUES
(1, 'Anusha', 'Data Engineering', 'Data Engineer', 'South', 3, 125000, 155000, 24, 9.4),
(2, 'Rahul', 'Data Engineering', 'Data Engineer', 'South', 2, 75000, 95000, 25, 8.6),
(3, 'Priya', 'Data Engineering', 'Senior Data Engineer', 'South', 5, 115000, 145000, 29, 9.5),
(4, 'Kiran', 'Data Analytics', 'Data Analyst', 'South', 3, 70000, 85000, 26, 8.2),

(5, 'Arjun', 'Data Engineering', 'Senior Data Engineer', 'North', 6, 145000, 180000, 30, 9.6),
(6, 'Sneha', 'Data Analytics', 'Data Analyst', 'North', 3, 80000, 105000, 26, 8.7),
(7, 'Vikram', 'Data Engineering', 'Data Engineer', 'North', 5, 125000, 160000, 29, 9.3),
(8, 'Neha', 'Data Engineering', 'Cloud Data Engineer', 'North', 4, 115000, 135000, 27, 9.0),

(9, 'Rohit', 'Data Engineering', 'Data Engineer', 'East', 2, 72000, 90000, 24, 8.1),
(10, 'Kavya', 'Data Engineering', 'Senior Data Engineer', 'East', 7, 160000, 210000, 32, 9.8),
(11, 'Manoj', 'Data Analytics', 'Data Analyst', 'East', 3, 78000, 100000, 25, 8.4),
(12, 'Divya', 'Data Engineering', 'Data Engineer', 'East', 4, 105000, 145000, 28, 9.1),

(13, 'Suresh', 'Data Engineering', 'Data Engineer', 'West', 1, 65000, 75000, 23, 7.8),
(14, 'Meena', 'Data Engineering', 'Senior Data Engineer', 'West', 5, 130000, 155000, 29, 9.4),
(15, 'Akhil', 'Data Analytics', 'Data Analyst', 'West', 2, 76000, 88000, 25, 8.3),
(16, 'Pooja', 'Data Engineering', 'Cloud Data Engineer', 'West', 4, 118000, 150000, 27, 9.0),

(17, 'Varun', 'Data Engineering', 'Data Engineer', 'Central', 3, 98000, 125000, 26, 8.9),
(18, 'Nisha', 'Data Engineering', 'Senior Data Engineer', 'Central', 6, 150000, 190000, 31, 9.7),
(19, 'Ajay', 'Data Analytics', 'Data Analyst', 'Central', 2, 68000, 82000, 24, 8.0),
(20, 'Riya', 'Data Engineering', 'Data Engineer', 'Central', 4, 112000, 135000, 27, 9.2);


-- 3. Check all records

SELECT *
FROM employees;
-- ============================================
-- TASK 1: Non-Correlated Subquery
-- Find employees whose sales are above average
-- ============================================

SELECT *
FROM employees
WHERE sales_amount > (
    SELECT AVG(sales_amount)
    FROM employees
);
-- ============================================
-- TASK 2: CORRELATED SUBQUERY
-- Find the top performer in each region
-- ============================================

SELECT
    e1.employee_name,
    e1.department,
    e1.job_role,
    e1.region,
    e1.performance_score
FROM employees e1
WHERE e1.performance_score = (
    SELECT MAX(e2.performance_score)
    FROM employees e2
    WHERE e2.region = e1.region
);
-- ============================================
-- TASK 3: CTE USING WITH CLAUSE
-- Find employees whose sales are above average
-- ============================================

WITH average_sales AS (
    SELECT AVG(sales_amount) AS avg_sales
    FROM employees
)
SELECT
    employee_name,
    department,
    region,
    sales_amount
FROM employees
WHERE sales_amount > (
    SELECT avg_sales
    FROM average_sales
);
-- ============================================
-- TASK 4: CHAIN 2 CTEs
-- Find regions with total sales above average
-- ============================================

WITH regional_sales AS (
    SELECT
        region,
        SUM(sales_amount) AS total_sales
    FROM employees
    GROUP BY region
),
high_sales_regions AS (
    SELECT
        region,
        total_sales
    FROM regional_sales
    WHERE total_sales > (
        SELECT AVG(total_sales)
        FROM regional_sales
    )
)
SELECT *
FROM high_sales_regions;