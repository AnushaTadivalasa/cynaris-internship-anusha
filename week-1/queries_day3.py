import sqlite3

# Create in-memory database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Read SQL file
with open("week-1/queries_day3.sql", "r", encoding="utf-8") as file:
    sql_script = file.read()

# Execute SQL script
cursor.executescript(sql_script)

print("Day 3 SQL executed successfully!")

conn.close()

import sqlite3

# Create in-memory database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Read SQL file
with open("week-1/queries_day3.sql", "r", encoding="utf-8") as file:
    sql_script = file.read()

# Execute table creation and INSERT statements
cursor.executescript(sql_script)

print("Day 3 SQL executed successfully!\n")


# 1. COUNT(*)
cursor.execute("""
SELECT COUNT(*) AS total_sales
FROM sales;
""")

print("1. TOTAL SALES:")
print(cursor.fetchall())


# 2. COUNT(column)
cursor.execute("""
SELECT COUNT(customer_id) AS customers_with_id
FROM sales;
""")

print("\n2. NON-NULL CUSTOMER IDs:")
print(cursor.fetchall())


# 3. COUNT(DISTINCT region)
cursor.execute("""
SELECT COUNT(DISTINCT region) AS unique_regions
FROM sales;
""")

print("\n3. UNIQUE REGIONS:")
print(cursor.fetchall())


# 4. SUM()
cursor.execute("""
SELECT SUM(sales_amount) AS total_sales_amount
FROM sales;
""")

print("\n4. TOTAL SALES AMOUNT:")
print(cursor.fetchall())


# 5. AVG()
cursor.execute("""
SELECT AVG(sales_amount) AS average_sales
FROM sales;
""")

print("\n5. AVERAGE SALES:")
print(cursor.fetchall())


# 6. MAX() and MIN()
cursor.execute("""
SELECT
    MAX(sales_amount) AS highest_sale,
    MIN(sales_amount) AS lowest_sale
FROM sales;
""")

print("\n6. HIGHEST AND LOWEST SALE:")
print(cursor.fetchall())


# 7. GROUP BY region
cursor.execute("""
SELECT
    region,
    COUNT(*) AS total_sales
FROM sales
GROUP BY region;
""")

print("\n7. SALES COUNT BY REGION:")
for row in cursor.fetchall():
    print(row)


# 8. GROUP BY region - SUM
cursor.execute("""
SELECT
    region,
    SUM(sales_amount) AS region_sales
FROM sales
GROUP BY region;
""")

print("\n8. TOTAL SALES BY REGION:")
for row in cursor.fetchall():
    print(row)


# 9. GROUP BY region, category
cursor.execute("""
SELECT
    region,
    category,
    COUNT(*) AS total_sales
FROM sales
GROUP BY region, category;
""")

print("\n9. SALES BY REGION AND CATEGORY:")
for row in cursor.fetchall():
    print(row)


# 10. WHERE + GROUP BY + HAVING
cursor.execute("""
SELECT
    category,
    COUNT(*) AS total_sales
FROM sales
WHERE region = 'South'
GROUP BY category
HAVING COUNT(*) > 2;
""")

print("\n10. SOUTH CATEGORIES WITH MORE THAN 2 SALES:")
for row in cursor.fetchall():
    print(row)


# 11. GROUP BY month
cursor.execute("""
SELECT
    SUBSTR(sale_date, 1, 7) AS sale_month,
    SUM(sales_amount) AS monthly_sales
FROM sales
GROUP BY SUBSTR(sale_date, 1, 7);
""")

print("\n11. MONTHLY SALES:")
for row in cursor.fetchall():
    print(row)


# 12. HAVING with SUM()
cursor.execute("""
SELECT
    region,
    SUM(sales_amount) AS total_sales
FROM sales
GROUP BY region
HAVING SUM(sales_amount) > 200000;
""")

print("\n12. REGIONS WITH SALES GREATER THAN 200000:")
for row in cursor.fetchall():
    print(row)


# 13. WINDOW FUNCTION
cursor.execute("""
SELECT
    region,
    category,
    sales_amount,
    SUM(sales_amount) OVER (
        PARTITION BY region
    ) AS region_total
FROM sales;
""")

print("\n13. WINDOW FUNCTION - REGION TOTAL:")
for row in cursor.fetchall():
    print(row)


conn.close()