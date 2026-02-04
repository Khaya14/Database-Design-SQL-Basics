-- ============================================================================
-- Q5: JOIN Semantics & Join Strategies - SQL Examples
-- ============================================================================
-- This file contains practical SQL examples demonstrating:
-- 1. Different JOIN types (INNER, LEFT, RIGHT, FULL, CROSS)
-- 2. NULL behavior in joins
-- 3. Join algorithm hints and optimization
--
-- Database: SQL Server Compatible (also works with most SQL databases)
-- Author: Week 4 Database Research
-- Date: February 2026
-- ============================================================================

-- ----------------------------------------------------------------------------
-- SETUP: Create sample tables for demonstration
-- ----------------------------------------------------------------------------

-- Create Employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dept_id INT,
    salary DECIMAL(10, 2),
    hire_date DATE
);

-- Create Departments table
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);

-- Insert sample data into employees
INSERT INTO employees (employee_id, name, dept_id, salary, hire_date) VALUES
(1, 'Alice Johnson', 10, 50000.00, '2020-01-15'),
(2, 'Bob Smith', 20, 60000.00, '2019-03-22'),
(3, 'Carol White', 10, 55000.00, '2021-06-10'),
(4, 'David Brown', 30, 70000.00, '2018-11-05'),
(5, 'Eve Davis', NULL, 45000.00, '2022-02-14'),  -- No department assigned
(6, 'Frank Miller', 40, 48000.00, '2020-08-20'); -- Department doesn't exist

-- Insert sample data into departments
INSERT INTO departments (dept_id, dept_name, location) VALUES
(10, 'Sales', 'New York'),
(20, 'Marketing', 'Los Angeles'),
(30, 'IT', 'San Francisco'),
(50, 'Legal', 'Chicago');  -- Department with no employees

-- ----------------------------------------------------------------------------
-- SECTION 1: INNER JOIN
-- ----------------------------------------------------------------------------
-- Returns only rows with matching values in both tables

-- Basic INNER JOIN
SELECT 
    e.employee_id,
    e.name,
    e.salary,
    d.dept_name,
    d.location
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- Result: 4 rows (Alice, Bob, Carol, David)
-- Eve excluded (dept_id is NULL)
-- Frank excluded (dept_id 40 doesn't exist in departments)
-- Legal department excluded (no employees)

-- INNER JOIN with additional conditions
SELECT 
    e.name,
    d.dept_name,
    e.salary
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > 50000
ORDER BY e.salary DESC;

-- Multiple INNER JOINs
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    dept_id INT
);

INSERT INTO projects VALUES
(1, 'Project Alpha', 10),
(2, 'Project Beta', 20),
(3, 'Project Gamma', 30);

SELECT 
    e.name AS employee_name,
    d.dept_name,
    p.project_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
INNER JOIN projects p ON d.dept_id = p.dept_id;

-- ----------------------------------------------------------------------------
-- SECTION 2: LEFT (OUTER) JOIN
-- ----------------------------------------------------------------------------
-- Returns all rows from left table, with NULLs for non-matching right table

-- Basic LEFT JOIN
SELECT 
    e.employee_id,
    e.name,
    e.dept_id AS emp_dept_id,
    d.dept_id AS dept_dept_id,
    d.dept_name,
    d.location
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- Result: All 6 employees
-- Eve: dept_name and location are NULL
-- Frank: dept_name and location are NULL

-- Find employees without departments (LEFT JOIN with NULL check)
SELECT 
    e.employee_id,
    e.name,
    e.dept_id
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;

-- Result: Eve and Frank (no matching departments)

-- LEFT JOIN with aggregation
SELECT 
    d.dept_name,
    COUNT(e.employee_id) AS employee_count,
    AVG(e.salary) AS avg_salary
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name;

-- Result includes Legal department with 0 employees

-- ----------------------------------------------------------------------------
-- SECTION 3: RIGHT (OUTER) JOIN
-- ----------------------------------------------------------------------------
-- Returns all rows from right table, with NULLs for non-matching left table

-- Basic RIGHT JOIN
SELECT 
    e.employee_id,
    e.name,
    d.dept_id,
    d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;

-- Result: Shows all departments
-- Legal department has NULL employee_id and name

-- Find departments without employees
SELECT 
    d.dept_id,
    d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id
WHERE e.employee_id IS NULL;

-- Result: Legal department (dept_id 50)

-- Note: RIGHT JOIN can always be rewritten as LEFT JOIN by swapping tables
-- This RIGHT JOIN:
SELECT * FROM employees e RIGHT JOIN departments d ON e.dept_id = d.dept_id;
-- Is equivalent to this LEFT JOIN:
SELECT * FROM departments d LEFT JOIN employees e ON d.dept_id = e.dept_id;

-- ----------------------------------------------------------------------------
-- SECTION 4: FULL OUTER JOIN
-- ----------------------------------------------------------------------------
-- Returns all rows from both tables, with NULLs where there's no match

-- Basic FULL OUTER JOIN
SELECT 
    e.employee_id,
    e.name,
    e.dept_id AS emp_dept_id,
    d.dept_id AS dept_dept_id,
    d.dept_name
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.dept_id;

-- Result: All employees AND all departments
-- Shows mismatches in both directions:
-- - Employees without valid departments (Eve, Frank)
-- - Departments without employees (Legal)

-- Find all mismatches (employees without departments OR departments without employees)
SELECT 
    COALESCE(e.name, 'No Employee') AS employee_name,
    COALESCE(d.dept_name, 'No Department') AS department_name,
    CASE 
        WHEN e.employee_id IS NULL THEN 'Department has no employees'
        WHEN d.dept_id IS NULL THEN 'Employee has no department'
        ELSE 'Match found'
    END AS match_status
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.dept_id
WHERE e.employee_id IS NULL OR d.dept_id IS NULL;

-- Data reconciliation use case
-- Find orphaned records in both tables
SELECT 
    'Employee without department' AS issue_type,
    e.employee_id AS id,
    e.name AS name,
    NULL AS dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL AND e.dept_id IS NOT NULL

UNION ALL

SELECT 
    'Department without employees' AS issue_type,
    d.dept_id AS id,
    NULL AS name,
    d.dept_name
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
WHERE e.employee_id IS NULL;

-- ----------------------------------------------------------------------------
-- SECTION 5: CROSS JOIN (Cartesian Product)
-- ----------------------------------------------------------------------------
-- Combines every row from first table with every row from second table

-- Basic CROSS JOIN
SELECT 
    e.name AS employee_name,
    d.dept_name
FROM employees e
CROSS JOIN departments d;

-- Result: 6 employees × 4 departments = 24 rows

-- Practical use case: Generate all possible combinations
-- Example: Create all possible employee-project assignments for planning
SELECT 
    e.name AS employee,
    p.project_name AS project
FROM employees e
CROSS JOIN projects p
WHERE e.dept_id IS NOT NULL  -- Only employees with departments
ORDER BY e.name, p.project_name;

-- Generate date ranges (useful for reporting)
CREATE TABLE date_parts (day_name VARCHAR(10));
INSERT INTO date_parts VALUES ('Monday'), ('Tuesday'), ('Wednesday'), 
                              ('Thursday'), ('Friday');

CREATE TABLE time_slots (time_slot VARCHAR(20));
INSERT INTO time_slots VALUES ('Morning'), ('Afternoon'), ('Evening');

-- Create all possible day-time combinations
-- SQL Server compatible version (using CONCAT instead of ||)
SELECT 
    d.day_name,
    t.time_slot,
    CONCAT(d.day_name, ' ', t.time_slot) AS full_slot
FROM date_parts d
CROSS JOIN time_slots t
ORDER BY 
    CASE d.day_name 
        WHEN 'Monday' THEN 1
        WHEN 'Tuesday' THEN 2
        WHEN 'Wednesday' THEN 3
        WHEN 'Thursday' THEN 4
        WHEN 'Friday' THEN 5
    END,
    CASE t.time_slot
        WHEN 'Morning' THEN 1
        WHEN 'Afternoon' THEN 2
        WHEN 'Evening' THEN 3
    END;

-- ----------------------------------------------------------------------------
-- SECTION 6: NULL Behavior in JOINs
-- ----------------------------------------------------------------------------

-- Demonstrate NULL = NULL is not TRUE
SELECT 
    e1.name AS employee1,
    e2.name AS employee2
FROM employees e1
JOIN employees e2 ON e1.dept_id = e2.dept_id
WHERE e1.employee_id < e2.employee_id;

-- Result: Eve (dept_id = NULL) doesn't join with herself
-- Because NULL = NULL evaluates to UNKNOWN, not TRUE

-- To explicitly join on NULL values, use IS NULL
SELECT 
    e1.name AS employee1,
    e2.name AS employee2,
    e1.dept_id
FROM employees e1
JOIN employees e2 ON (
    (e1.dept_id = e2.dept_id) OR 
    (e1.dept_id IS NULL AND e2.dept_id IS NULL)
)
WHERE e1.employee_id < e2.employee_id;

-- Using COALESCE to handle NULLs in join conditions
SELECT 
    e.name,
    d.dept_name,
    COALESCE(d.dept_name, 'Unassigned') AS dept_display
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- ----------------------------------------------------------------------------
-- SECTION 7: JOIN Algorithm Hints (SQL Server specific)
-- ----------------------------------------------------------------------------

-- SQL Server uses query hints instead of SET commands

-- Force nested loop join
SELECT 
    e.name, 
    d.dept_name
FROM employees e
INNER LOOP JOIN departments d ON e.dept_id = d.dept_id
OPTION (FORCE ORDER);

-- Force hash join
SELECT 
    e.name, 
    d.dept_name
FROM employees e
INNER HASH JOIN departments d ON e.dept_id = d.dept_id;

-- Force merge join
SELECT 
    e.name, 
    d.dept_name
FROM employees e
INNER MERGE JOIN departments d ON e.dept_id = d.dept_id;

-- View execution plan (SQL Server)
-- In SSMS, press Ctrl+L before running, or use:
SET SHOWPLAN_ALL ON;
GO
SELECT 
    e.name,
    d.dept_name,
    e.salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE d.location = 'New York'
ORDER BY e.salary DESC;
GO
SET SHOWPLAN_ALL OFF;
GO

-- Alternative: Actual execution plan with statistics
SET STATISTICS IO ON;
SET STATISTICS TIME ON;

SELECT 
    e.name,
    d.dept_name,
    e.salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE d.location = 'New York'
ORDER BY e.salary DESC;

SET STATISTICS IO OFF;
SET STATISTICS TIME OFF;

-- ----------------------------------------------------------------------------
-- SECTION 8: JOIN Performance Examples
-- ----------------------------------------------------------------------------

-- Create indexes for optimal join performance
CREATE INDEX idx_employees_dept_id ON employees(dept_id);
CREATE INDEX idx_departments_dept_id ON departments(dept_id);

-- View execution plan with actual statistics
-- Use SSMS graphical execution plan (Ctrl+M) or:
SET STATISTICS IO ON;
SET STATISTICS TIME ON;

SELECT 
    e.name,
    d.dept_name,
    e.salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE d.location = 'New York'
ORDER BY e.salary DESC;

SET STATISTICS IO OFF;
SET STATISTICS TIME OFF;

-- Compare with and without indexes
DROP INDEX idx_employees_dept_id ON employees;

-- Run again to see performance difference
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

-- Recreate index
CREATE INDEX idx_employees_dept_id ON employees(dept_id);

-- ----------------------------------------------------------------------------
-- SECTION 9: Self-JOIN Examples
-- ----------------------------------------------------------------------------

-- Create manager relationship
ALTER TABLE employees ADD manager_id INT;

UPDATE employees SET manager_id = 1 WHERE employee_id IN (2, 3);
UPDATE employees SET manager_id = 2 WHERE employee_id = 6;

-- Find employees and their managers
SELECT 
    e.name AS employee_name,
    m.name AS manager_name,
    e.salary AS employee_salary,
    m.salary AS manager_salary
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;

-- Find employees who earn more than their managers
SELECT 
    e.name AS employee_name,
    e.salary AS employee_salary,
    m.name AS manager_name,
    m.salary AS manager_salary
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
WHERE e.salary > m.salary;

-- ----------------------------------------------------------------------------
-- SECTION 10: Advanced JOIN Patterns
-- ----------------------------------------------------------------------------

-- Multiple conditions in JOIN
SELECT 
    e.name,
    d.dept_name
FROM employees e
JOIN departments d 
    ON e.dept_id = d.dept_id 
    AND d.location = 'New York';

-- JOIN with inequality conditions
SELECT 
    e1.name AS employee1,
    e1.salary AS salary1,
    e2.name AS employee2,
    e2.salary AS salary2
FROM employees e1
JOIN employees e2 
    ON e1.dept_id = e2.dept_id 
    AND e1.salary < e2.salary
WHERE e1.dept_id IS NOT NULL
ORDER BY e1.dept_id, e1.salary;

-- OUTER APPLY (SQL Server specific - similar to LATERAL JOIN)
SELECT 
    d.dept_name,
    top_emp.name,
    top_emp.salary
FROM departments d
OUTER APPLY (
    SELECT TOP 1 e.name, e.salary
    FROM employees e
    WHERE e.dept_id = d.dept_id
    ORDER BY e.salary DESC
) AS top_emp;

-- CROSS APPLY (only returns rows where subquery produces results)
SELECT 
    d.dept_name,
    top_emp.name,
    top_emp.salary
FROM departments d
CROSS APPLY (
    SELECT TOP 1 e.name, e.salary
    FROM employees e
    WHERE e.dept_id = d.dept_id
    ORDER BY e.salary DESC
) AS top_emp;

-- ----------------------------------------------------------------------------
-- SECTION 11: Common JOIN Patterns and Best Practices
-- ----------------------------------------------------------------------------

-- Pattern 1: Find records that exist in A but not in B
SELECT e.*
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL AND e.dept_id IS NOT NULL;

-- Pattern 2: Find records that exist in B but not in A
SELECT d.*
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
WHERE e.employee_id IS NULL;

-- Pattern 3: Find records that exist in either A or B but not both
SELECT 
    COALESCE(e.employee_id, -1) AS emp_id,
    COALESCE(d.dept_id, -1) AS dept_id,
    e.name,
    d.dept_name,
    CASE 
        WHEN e.employee_id IS NULL THEN 'Only in Departments'
        WHEN d.dept_id IS NULL THEN 'Only in Employees'
    END AS exclusivity
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.dept_id
WHERE e.employee_id IS NULL OR d.dept_id IS NULL;

-- Pattern 4: Multiple table joins with filtering
SELECT 
    e.name AS employee,
    d.dept_name AS department,
    p.project_name AS project,
    e.salary
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
INNER JOIN projects p ON d.dept_id = p.dept_id
WHERE e.salary > 50000
ORDER BY e.salary DESC, p.project_name;

-- ----------------------------------------------------------------------------
-- CLEANUP
-- ----------------------------------------------------------------------------

DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS date_parts;
DROP TABLE IF EXISTS time_slots;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

-- ============================================================================
-- END OF Q5 EXAMPLES
-- ============================================================================