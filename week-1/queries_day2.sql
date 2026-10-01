-- Departments table
CREATE TABLE departments (
    dept_id INTEGER,
    dept_name TEXT,
    location TEXT,
    manager TEXT,
    budget INTEGER
);

INSERT INTO departments VALUES
(1, 'Data', 'Hyderabad', 'Meena', 500000),
(2, 'HR', 'Chennai', 'Ravi', 300000),
(3, 'Finance', 'Bangalore', 'Priya', 400000),
(4, 'IT', 'Pune', 'Kiran', 600000),
(5, 'Sales', 'Mumbai', 'Sita', 450000),
(6, 'Marketing', 'Delhi', 'Arun', 350000),
(7, 'Support', 'Hyderabad', 'Divya', 250000),
(8, 'Admin', 'Chennai', 'Rahul', 200000),
(9, 'Testing', 'Pune', 'Sneha', 320000),
(10, 'Security', 'Bangalore', 'Vijay', 550000);
-- Employees table
CREATE TABLE employees (
    emp_id INTEGER,
    emp_name TEXT,
    dept_id INTEGER,
    job_role TEXT,
    salary INTEGER,
    manager_id INTEGER
);

INSERT INTO employees VALUES
(101, 'Anusha', 1, 'Data Engineer', 70000, NULL),
(102, 'Sita', 2, 'HR Executive', 35000, 101),
(103, 'Priya', 1, 'Data Analyst', 55000, 101),
(104, 'Kiran', 3, 'Accountant', 40000, 103),
(105, 'Anil', 4, 'Developer', 60000, 104),
(106, 'Divya', 5, 'Sales Executive', 38000, 101),
(107, 'Meena', 6, 'Marketing Analyst', 42000, 101),
(108, 'Rahul', 7, 'Support Engineer', 36000, 101),
(109, 'Sneha', 4, 'Software Developer', 58000, 104),
(110, 'Vijay', 11, 'Security Analyst', 50000, 101);
-- 3. INNER JOIN
-- Only matching records from both tables
-- ==========================================
SELECT
    e.emp_name,
    e.job_role,
    d.dept_name
FROM employees AS e
INNER JOIN departments AS d
    ON e.dept_id = d.dept_id;


-- ==========================================
-- 4. LEFT JOIN
-- All employees + matching departments
-- ==========================================

SELECT
    e.emp_name,
    e.job_role,
    d.dept_name
FROM employees AS e
LEFT JOIN departments AS d
    ON e.dept_id = d.dept_id;


-- ==========================================
-- 5. RIGHT JOIN
-- All departments + matching employees
-- ==========================================

SELECT
    e.emp_name,
    e.job_role,
    d.dept_name
FROM employees AS e
RIGHT JOIN departments AS d
    ON e.dept_id = d.dept_id;


-- ==========================================
-- 6. FULL OUTER JOIN
-- All employees + all departments
-- ==========================================

SELECT
    e.emp_name,
    e.job_role,
    d.dept_name
FROM employees AS e
FULL OUTER JOIN departments AS d
    ON e.dept_id = d.dept_id;


-- ==========================================
-- 7. DUPLICATE ROWS CAUSED BY JOIN
-- ==========================================

CREATE TABLE department_locations (
    dept_id INTEGER,
    location TEXT
);

INSERT INTO department_locations VALUES
(1, 'Hyderabad'),
(1, 'Secunderabad'),
(2, 'Chennai'),
(3, 'Bangalore');


-- Data department has 2 employees
-- and 2 locations.
-- Therefore 2 x 2 = 4 rows.

SELECT
    d.dept_name,
    e.emp_name,
    dl.location
FROM departments AS d
JOIN employees AS e
    ON d.dept_id = e.dept_id
JOIN department_locations AS dl
    ON d.dept_id = dl.dept_id
WHERE d.dept_id = 1;


-- ==========================================
-- 8. SELF JOIN
-- Find each employee and their manager
-- ==========================================

SELECT
    e.emp_name AS employee,
    m.emp_name AS manager
FROM employees AS e
LEFT JOIN employees AS m