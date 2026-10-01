-- database: :memory:
-- Week 1 - Day 3
-- SQL Aggregations — GROUP BY & HAVING


-- =====================================================
-- SALES TABLE
-- =====================================================

CREATE TABLE sales (
    sale_id INTEGER,
    sale_date TEXT,
    region TEXT,
    category TEXT,
    product TEXT,
    quantity INTEGER,
    sales_amount INTEGER,
    customer_id INTEGER
);


-- =====================================================
-- INSERT SAMPLE DATA
-- =====================================================

INSERT INTO sales VALUES
(1,  '2026-01-05', 'North', 'Electronics', 'Laptop',   2, 120000, 101),
(2,  '2026-01-07', 'South', 'Electronics', 'Mobile',   3,  90000, 102),
(3,  '2026-01-10', 'South', 'Furniture',   'Chair',    5,  25000, 103),
(4,  '2026-01-12', 'East',  'Electronics', 'Laptop',   1,  60000, 104),
(5,  '2026-01-15', 'West',  'Furniture',   'Table',    2,  30000, 105),
(6,  '2026-01-18', 'South', 'Electronics', 'Laptop',   2, 120000, 106),
(7,  '2026-02-02', 'North', 'Furniture',   'Chair',    4,  20000, 107),
(8,  '2026-02-05', 'South', 'Electronics', 'Mobile',   2,  60000, 108),
(9,  '2026-02-08', 'East',  'Furniture',   'Table',    3,  45000, 109),
(10, '2026-02-10', 'West',  'Electronics', 'Laptop',   1,  60000, 110),
(11, '2026-02-15', 'South', 'Furniture',   'Chair',    6,  30000, 111),
(12, '2026-02-18', 'North', 'Electronics', 'Mobile',   4, 120000, 112),
(13, '2026-03-01', 'East',  'Electronics', 'Mobile',   3,  90000, 113),
(14, '2026-03-04', 'South', 'Furniture',   'Table',    2,  30000, 114),
(15, '2026-03-07', 'West',  'Electronics', 'Mobile',   5, 150000, 115),
(16, '2026-03-10', 'North', 'Furniture',   'Table',    2,  30000, 116),
(17, '2026-03-15', 'South', 'Electronics', 'Laptop',   1,  60000, 117),
(18, '2026-03-18', 'East',  'Furniture',   'Chair',    4,  20000, 118),
(19, '2026-03-20', 'West',  'Furniture',   'Chair',    3,  15000, 119),
(20, '2026-03-25', 'South', 'Electronics', 'Mobile',   2,  60000, 120);


-- =====================================================
-- 1. COUNT(*)
-- Total number of sales records
-- =====================================================

SELECT
    COUNT(*) AS total_sales
FROM sales;


-- =====================================================
-- 2. COUNT(column)
-- Number of non-NULL customer IDs
-- =====================================================

SELECT
    COUNT(customer_id) AS customers_with_id
FROM sales;


-- =====================================================
-- 3. COUNT(DISTINCT column)
-- Number of unique regions
-- =====================================================

SELECT
    COUNT(DISTINCT region) AS unique_regions
FROM sales;


-- =====================================================
-- 4. SUM()
-- Total sales amount
-- =====================================================

SELECT
    SUM(sales_amount) AS total_sales_amount
FROM sales;


-- =====================================================
-- 5. AVG()
-- Average sales amount
-- =====================================================

SELECT
    AVG(sales_amount) AS average_sales
FROM sales;


-- =====================================================
-- 6. MAX() and MIN()
-- Highest and lowest sale
-- =====================================================

SELECT
    MAX(sales_amount) AS highest_sale,
    MIN(sales_amount) AS lowest_sale
FROM sales;


-- =====================================================
-- 7. GROUP BY region
-- Total sales records in each region
-- =====================================================

SELECT
    region,
    COUNT(*) AS total_sales
FROM sales
GROUP BY region;


-- =====================================================
-- 8. GROUP BY region
-- Total sales amount for each region
-- =====================================================

SELECT
    region,
    SUM(sales_amount) AS region_sales
FROM sales
GROUP BY region;


-- =====================================================
-- 9. GROUP BY region, category
-- Number of sales for each category in each region
-- =====================================================

SELECT
    region,
    category,
    COUNT(*) AS total_sales
FROM sales
GROUP BY region, category;


-- =====================================================
-- 10. WHERE + GROUP BY + HAVING
-- South region categories with more than 2 sales
-- =====================================================

SELECT
    category,
    COUNT(*) AS total_sales
FROM sales
WHERE region = 'South'
GROUP BY category
HAVING COUNT(*) > 2;


-- =====================================================
-- 11. GROUP BY month
-- Total sales amount for each month
-- =====================================================

SELECT
    SUBSTR(sale_date, 1, 7) AS sale_month,
    SUM(sales_amount) AS monthly_sales
FROM sales
GROUP BY SUBSTR(sale_date, 1, 7);


-- =====================================================
-- 12. HAVING with SUM()
-- Regions whose total sales are greater than 200000
-- =====================================================

SELECT
    region,
    SUM(sales_amount) AS total_sales
FROM sales
GROUP BY region
HAVING SUM(sales_amount) > 200000;


-- =====================================================
-- 13. WINDOW FUNCTION
-- Total sales of each region while keeping every row
-- =====================================================

SELECT
    region,
    category,
    sales_amount,
    SUM(sales_amount) OVER (
        PARTITION BY region
    ) AS region_total
FROM sales;