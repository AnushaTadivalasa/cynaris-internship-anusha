# SQL Fundamentals — SELECT, FROM, WHERE - Starter Template
# Day 1 | Week 1

import sys
print(f"Python {sys.version}")

# Write your code here...
import sqlite3
import pandas as pd
#Create in-memory sales database

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE sales (
id       INTEGER PRIMARY KEY,
product  TEXT,
region   TEXT,
amount   DECIMAL(10,2),
sale_date DATE,
quantity INTEGER,
discount DECIMAL(4,2)
)
''')


cursor.executemany("INSERT INTO sales VALUES (?,?,?,?,?,?,?)", [
(1,  'Laptop',     'North', 85000, '2026-01-15', 2, 0.05),
(2,  'Phone',      'South', 45000, '2026-02-20', 5, 0.10),
(3,  'Tablet',     'East',  32000, '2026-01-28', 3, 0.00),
(4,  'Laptop',     'West',  85000, '2026-03-10', 1, 0.15),
(5,  'Phone',      'North', 45000, '2026-02-05', 4, 0.05),
(6,  'Headphones', 'South',  8000, '2026-03-15',10, 0.00),
(7,  'Tablet',     'North', 32000, '2026-04-01', 2, 0.08),
(8,  'Laptop',     'East',  85000, '2026-01-20', 3, 0.10),
(9,  'Phone',      'West',  45000, '2026-04-18', 6, 0.00),
(10, 'Headphones', 'East',   8000, '2026-02-28', 8, 0.05),
(11, 'Tablet',     'South', 32000, '2026-03-22', 1, 0.12),
(12, 'Laptop',     'South', 85000, '2026-05-10', 2, None),
])
conn.commit()


#--- Write your 10 SELECT queries below ---

# Example:

result = pd.read_sql("SELECT * FROM sales WHERE region = 'North'", conn)
print(result)
# Query 1: Select product and amount for Laptop sales

result = pd.read_sql(
    """
    SELECT product, amount
    FROM sales
    WHERE product = 'Laptop'
    """,
    conn
)

print(result)

# Query 2: Select sales where amount is greater than 50000

result = pd.read_sql(
    """
    SELECT product, region, amount
    FROM sales
    WHERE amount > 50000
    """,
    conn
)

print(result)
# Query 3: North region sales with amount greater than 40000

result = pd.read_sql(
    """
    SELECT product, region, amount
    FROM sales
    WHERE region = 'North'
    AND amount > 40000
    """,
    conn
)

print(result)
# Query 4: Select North or South region sales

result = pd.read_sql(
    """
    SELECT product, region, amount
    FROM sales
    WHERE region = 'North'
    OR region = 'South'
    """,
    conn
)

print(result)
# Query 5: Select sales that are not from North region

result = pd.read_sql(
    """
    SELECT product, region, amount
    FROM sales
    WHERE NOT region = 'North'
    """,
    conn
)

print(result)
# Query 6: Select products starting with "Lap"

result = pd.read_sql(
    """
    SELECT product, region, amount
    FROM sales
    WHERE product LIKE 'Lap%'
    """,
    conn
)

print(result)
# Query 7: Select sales from North or South regions

result = pd.read_sql(
    """
    SELECT product, region, amount
    FROM sales
    WHERE region IN ('North', 'South')
    """,
    conn
)

print(result)
# Query 8: Select sales with amount between 30000 and 50000

result = pd.read_sql(
    """
    SELECT product, region, amount
    FROM sales
    WHERE amount BETWEEN 30000 AND 50000
    """,
    conn
)

print(result)
# Query 9: Find sales where discount is missing

result = pd.read_sql(
    """
    SELECT product, region, amount, discount
    FROM sales
    WHERE discount IS NULL
    """,
    conn
)

print(result)
# Query 10: Select sales that are not from South region

result = pd.read_sql(
    """
    SELECT product, region, amount
    FROM sales
    WHERE region != 'South'
    """,
    conn
)

print(result)
# Export one result to CSV
# Export one result to CSV

north_sales = pd.read_sql(
    """
    SELECT *
    FROM sales
    WHERE region = 'North'
    """,
    conn
)

north_sales.to_csv('north_sales.csv', index=False)

print("Exported to north_sales.csv")

# result.to_csv('north_sales.csv', index=False)
# print("Exported to north_sales.csv")