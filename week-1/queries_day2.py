import sqlite3

# Create SQLite database
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# Create departments table
cursor.execute("""
CREATE TABLE departments (
    dept_id INTEGER,
    dept_name TEXT,
    location TEXT,
    manager TEXT,
    budget INTEGER
)
""")

# Insert departments data
cursor.executemany("""
INSERT INTO departments
VALUES (?, ?, ?, ?, ?)
""", [
    (1, 'Data', 'Hyderabad', 'Meena', 500000),
    (2, 'HR', 'Chennai', 'Ravi', 300000),
    (3, 'Finance', 'Bangalore', 'Priya', 400000),
    (4, 'IT', 'Pune', 'Kiran', 600000),
    (5, 'Sales', 'Mumbai', 'Sita', 450000),
    (6, 'Marketing', 'Delhi', 'Arun', 350000),
    (7, 'Support', 'Hyderabad', 'Divya', 250000),
    (8, 'Admin', 'Chennai', 'Rahul', 200000),
    (9, 'Testing', 'Pune', 'Sneha', 320000),
    (10, 'Security', 'Bangalore', 'Vijay', 550000)
])

# Create employees table
cursor.execute("""
CREATE TABLE employees (
    emp_id INTEGER,
    emp_name TEXT,
    dept_id INTEGER,
    job_role TEXT,
    salary INTEGER
)
""")

# Insert employees data
cursor.executemany("""
INSERT INTO employees
VALUES (?, ?, ?, ?, ?)
""", [
    (101, 'Anusha', 1, 'Data Engineer', 70000),
    (102, 'Sita', 2, 'HR Executive', 35000),
    (103, 'Priya', 1, 'Data Analyst', 55000),
    (104, 'Kiran', 3, 'Accountant', 40000),
    (105, 'Anil', 4, 'Developer', 60000),
    (106, 'Divya', 5, 'Sales Executive', 38000),
    (107, 'Meena', 6, 'Marketing Analyst', 42000),
    (108, 'Rahul', 7, 'Support Engineer', 36000),
    (109, 'Sneha', 4, 'Software Developer', 58000),
    (110, 'Vijay', 11, 'Security Analyst', 50000)
])

connection.commit()

print("Tables created and data inserted successfully!")
# Display departments
cursor.execute("SELECT * FROM departments")

rows = cursor.fetchall()

for row in rows:
    print(row)

# INNER JOIN
cursor.execute("""
SELECT
    e.emp_name,
    e.job_role,
    d.dept_name
FROM employees AS e
INNER JOIN departments AS d
    ON e.dept_id = d.dept_id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

# LEFT JOIN
cursor.execute("""
SELECT
    e.emp_name,
    e.job_role,
    d.dept_name
FROM employees AS e
LEFT JOIN departments AS d
    ON e.dept_id = d.dept_id
""")

rows = cursor.fetchall()

print("\nLEFT JOIN:")
for row in rows:
    print(row)

# RIGHT JOIN
cursor.execute("""
SELECT
    e.emp_name,
    e.job_role,
    d.dept_name
FROM employees AS e
RIGHT JOIN departments AS d
    ON e.dept_id = d.dept_id
""")

rows = cursor.fetchall()

print("\nRIGHT JOIN:")
for row in rows:
    print(row)

# FULL OUTER JOIN
cursor.execute("""
SELECT
    e.emp_name,
    e.job_role,
    d.dept_name
FROM employees AS e
FULL OUTER JOIN departments AS d
    ON e.dept_id = d.dept_id
""")

rows = cursor.fetchall()

print("\nFULL OUTER JOIN:")
for row in rows:
    print(row)

# Duplicate rows caused by JOIN

cursor.execute("DROP TABLE IF EXISTS department_locations")

cursor.execute("""
CREATE TABLE department_locations (
    dept_id INTEGER,
    location TEXT
)
""")

cursor.executemany("""
INSERT INTO department_locations (dept_id, location)
VALUES (?, ?)
""", [
    (1, "Hyderabad"),
    (1, "Secunderabad"),
    (2, "Chennai"),
    (3, "Bangalore")
])

# Duplicate rows example
cursor.execute("""
SELECT
    d.dept_name,
    e.emp_name,
    dl.location
FROM departments AS d
JOIN employees AS e
    ON d.dept_id = e.dept_id
JOIN department_locations AS dl
    ON d.dept_id = dl.dept_id
WHERE d.dept_id = 1
""")

print("\nDUPLICATE ROWS CAUSED BY JOIN:")

for row in cursor.fetchall():
    print(row)
# ==========================================
# SELF JOIN
# ==========================================

# Add manager_id column to employees table
cursor.execute("""
ALTER TABLE employees
ADD COLUMN manager_id INTEGER
""")

# Assign managers to employees
cursor.execute("""
UPDATE employees
SET manager_id = NULL
WHERE emp_id = 101
""")

cursor.execute("""
UPDATE employees
SET manager_id = 101
WHERE emp_id IN (102, 103, 106, 107, 108, 110)
""")

cursor.execute("""
UPDATE employees
SET manager_id = 103
WHERE emp_id = 104
""")

cursor.execute("""
UPDATE employees
SET manager_id = 104
WHERE emp_id IN (105, 109)
""")


# Self JOIN
query = """
SELECT
    e.emp_name AS employee,
    m.emp_name AS manager
FROM employees AS e
LEFT JOIN employees AS m
    ON e.manager_id = m.emp_id;
"""

cursor.execute(query)

print("\nSELF JOIN - EMPLOYEE AND MANAGER:")

for row in cursor.fetchall():
    print(row)
