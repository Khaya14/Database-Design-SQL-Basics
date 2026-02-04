-- ============================================================================
-- Q6: GROUP BY, Aggregation & Set Semantics - SQL Examples
-- ============================================================================
-- This file contains practical SQL examples demonstrating:
-- 1. GROUP BY mechanics and rules
-- 2. HAVING clause for filtering groups
-- 3. Aggregate functions (SUM, COUNT, AVG, MIN, MAX)
-- 4. COUNT(*) vs COUNT(column) behavior
-- 5. NULL handling in aggregates
-- 6. Common pitfalls and best practices
-- 7. DISTINCT with aggregation
--
-- Database: SQL Server Compatible (also works with PostgreSQL/MySQL)
-- Author: Week 4 Database Research
-- Date: February 2026
-- ============================================================================

-- ----------------------------------------------------------------------------
-- SETUP: Create sample tables for demonstration
-- ----------------------------------------------------------------------------

-- Create sales table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    customer_id INT,
    sale_date DATE,
    quantity INT,
    unit_price DECIMAL(10, 2),
    discount DECIMAL(5, 2),
    region VARCHAR(50)
);

-- Insert sample data
INSERT INTO sales (sale_id, product_id, customer_id, sale_date, quantity, unit_price, discount, region) VALUES
(1, 101, 1, '2024-01-15', 5, 100.00, 10.00, 'North'),
(2, 101, 2, '2024-01-16', 3, 100.00, NULL, 'North'),
(3, 102, 1, '2024-01-17', 2, 150.00, 5.00, 'South'),
(4, 103, 3, '2024-01-18', 10, 50.00, NULL, 'East'),
(5, 101, 2, '2024-01-19', 7, 100.00, 15.00, 'North'),
(6, 102, 4, '2024-01-20', NULL, 150.00, 20.00, 'West'),  -- NULL quantity
(7, 103, 1, '2024-01-21', 5, 50.00, NULL, 'East'),
(8, 104, 5, '2024-01-22', 8, 75.00, 10.00, 'South'),
(9, 101, NULL, '2024-01-23', 4, 100.00, NULL, 'North'),  -- NULL customer
(10, 102, 4, '2024-01-24', 6, 150.00, 25.00, 'West');

-- Create products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50)
);

INSERT INTO products VALUES
(101, 'Laptop', 'Electronics'),
(102, 'Desk', 'Furniture'),
(103, 'Mouse', 'Electronics'),
(104, 'Chair', 'Furniture');

-- Create customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO customers VALUES
(1, 'Alice Johnson', 'alice@example.com'),
(2, 'Bob Smith', NULL),  -- NULL email
(3, 'Carol White', 'carol@example.com'),
(4, 'David Brown', 'david@example.com'),
(5, 'Eve Davis', NULL);  -- NULL email

-- ----------------------------------------------------------------------------
-- SECTION 1: Basic GROUP BY
-- ----------------------------------------------------------------------------

-- Simple GROUP BY with COUNT
SELECT 
    region,
    COUNT(*) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;

-- Result: Shows number of sales per region
-- North: 4, East: 2, South: 2, West: 2

-- GROUP BY with multiple aggregate functions
SELECT 
    product_id,
    COUNT(*) AS num_sales,
    SUM(quantity) AS total_quantity,
    AVG(unit_price) AS avg_price,
    MIN(unit_price) AS min_price,
    MAX(unit_price) AS max_price
FROM sales
GROUP BY product_id
ORDER BY product_id;

-- GROUP BY multiple columns
SELECT 
    region,
    product_id,
    COUNT(*) AS sales_count,
    SUM(quantity * unit_price) AS total_revenue
FROM sales
GROUP BY region, product_id
ORDER BY region, product_id;

-- ----------------------------------------------------------------------------
-- SECTION 2: GROUP BY Rules and Common Errors
-- ----------------------------------------------------------------------------

-- CORRECT: All non-aggregated columns are in GROUP BY
SELECT 
    region,
    product_id,
    COUNT(*) AS sales_count,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY region, product_id;

-- INCORRECT: This would cause an error in most databases
-- Uncomment to see error:
/*
SELECT 
    region,
    product_id,
    customer_id,  -- ERROR: customer_id not in GROUP BY
    COUNT(*) AS sales_count
FROM sales
GROUP BY region, product_id;
*/

-- CORRECT way: Either add to GROUP BY or use aggregate
SELECT 
    region,
    product_id,
    COUNT(DISTINCT customer_id) AS unique_customers,
    COUNT(*) AS sales_count
FROM sales
GROUP BY region, product_id;

-- Using expressions in GROUP BY
SELECT 
    YEAR(sale_date) AS sale_year,
    MONTH(sale_date) AS sale_month,
    COUNT(*) AS monthly_sales,
    SUM(quantity * unit_price) AS monthly_revenue
FROM sales
GROUP BY YEAR(sale_date), MONTH(sale_date)
ORDER BY sale_year, sale_month;

-- ----------------------------------------------------------------------------
-- SECTION 3: HAVING Clause
-- ----------------------------------------------------------------------------

-- Find products with total sales > 500
SELECT 
    product_id,
    SUM(quantity * unit_price) AS total_sales
FROM sales
GROUP BY product_id
HAVING SUM(quantity * unit_price) > 500
ORDER BY total_sales DESC;

-- WHERE filters rows before grouping, HAVING filters after
SELECT 
    region,
    COUNT(*) AS sales_count,
    AVG(quantity) AS avg_quantity
FROM sales
WHERE sale_date >= '2024-01-18'  -- Filter individual rows
GROUP BY region
HAVING COUNT(*) >= 2  -- Filter groups
ORDER BY sales_count DESC;

-- Complex HAVING conditions
SELECT 
    product_id,
    COUNT(*) AS num_sales,
    AVG(quantity) AS avg_quantity,
    SUM(quantity * unit_price) AS total_revenue
FROM sales
GROUP BY product_id
HAVING COUNT(*) > 2 
   AND AVG(quantity) > 4
   AND SUM(quantity * unit_price) > 1000
ORDER BY total_revenue DESC;

-- HAVING with multiple aggregates
SELECT 
    region,
    COUNT(*) AS sales_count,
    AVG(unit_price) AS avg_price,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY region
HAVING COUNT(*) > 1 
   AND AVG(unit_price) > 80
ORDER BY sales_count DESC;

-- ----------------------------------------------------------------------------
-- SECTION 4: COUNT(*) vs COUNT(column)
-- ----------------------------------------------------------------------------

-- Demonstrate the difference
SELECT 
    'Total rows' AS metric,
    COUNT(*) AS count_value
FROM sales

UNION ALL

SELECT 
    'Rows with quantity',
    COUNT(quantity)  -- Excludes NULLs
FROM sales

UNION ALL

SELECT 
    'Rows with discount',
    COUNT(discount)  -- Excludes NULLs
FROM sales

UNION ALL

SELECT 
    'Rows with customer_id',
    COUNT(customer_id)  -- Excludes NULLs
FROM sales;

-- Practical example: Data quality check per product
SELECT 
    product_id,
    COUNT(*) AS total_sales,
    COUNT(quantity) AS sales_with_quantity,
    COUNT(*) - COUNT(quantity) AS sales_missing_quantity,
    COUNT(discount) AS sales_with_discount,
    COUNT(*) - COUNT(discount) AS sales_without_discount,
    COUNT(customer_id) AS sales_with_customer,
    COUNT(*) - COUNT(customer_id) AS anonymous_sales
FROM sales
GROUP BY product_id
ORDER BY product_id;

-- Using COUNT(column) to find completeness percentage
-- SQL Server compatible version
SELECT 
    region,
    COUNT(*) AS total_sales,
    COUNT(discount) AS sales_with_discount,
    ROUND(100.0 * COUNT(discount) / CAST(COUNT(*) AS DECIMAL), 2) AS discount_completeness_pct
FROM sales
GROUP BY region
ORDER BY region;

-- COUNT(DISTINCT column) - count unique values
SELECT 
    region,
    COUNT(*) AS total_sales,
    COUNT(DISTINCT customer_id) AS unique_customers,
    COUNT(DISTINCT product_id) AS unique_products,
    ROUND(CAST(COUNT(*) AS DECIMAL) / NULLIF(COUNT(DISTINCT customer_id), 0), 2) AS avg_sales_per_customer
FROM sales
GROUP BY region
ORDER BY region;

-- ----------------------------------------------------------------------------
-- SECTION 5: NULL Behavior in Aggregate Functions
-- ----------------------------------------------------------------------------

-- Create test table to demonstrate NULL behavior
CREATE TABLE test_nulls (
    id INT,
    value INT
);

INSERT INTO test_nulls VALUES
(1, 100),
(2, NULL),
(3, 200),
(4, NULL),
(5, 150);

-- NULL behavior in different aggregates
SELECT 
    'SUM' AS function_name,
    SUM(value) AS result,
    'Ignores NULLs: 100+200+150=450' AS explanation
FROM test_nulls

UNION ALL

SELECT 
    'AVG',
    AVG(value),
    'Average of non-NULL: 450/3=150'
FROM test_nulls

UNION ALL

SELECT 
    'COUNT(*)',
    COUNT(*),
    'Counts all rows: 5'
FROM test_nulls

UNION ALL

SELECT 
    'COUNT(value)',
    COUNT(value),
    'Counts non-NULL: 3'
FROM test_nulls

UNION ALL

SELECT 
    'MIN',
    MIN(value),
    'Minimum of non-NULL: 100'
FROM test_nulls

UNION ALL

SELECT 
    'MAX',
    MAX(value),
    'Maximum of non-NULL: 200'
FROM test_nulls;

-- What if ALL values are NULL?
CREATE TABLE all_nulls (value INT);
INSERT INTO all_nulls VALUES (NULL), (NULL), (NULL);

SELECT 
    SUM(value) AS sum_result,      -- Returns NULL
    AVG(value) AS avg_result,      -- Returns NULL
    MIN(value) AS min_result,      -- Returns NULL
    MAX(value) AS max_result,      -- Returns NULL
    COUNT(value) AS count_result,  -- Returns 0
    COUNT(*) AS count_all          -- Returns 3
FROM all_nulls;

-- ----------------------------------------------------------------------------
-- SECTION 6: Handling NULLs in Aggregation
-- ----------------------------------------------------------------------------

-- Include NULLs as zero using COALESCE
SELECT 
    product_id,
    SUM(quantity) AS sum_ignoring_nulls,
    SUM(COALESCE(quantity, 0)) AS sum_treating_nulls_as_zero,
    AVG(quantity) AS avg_ignoring_nulls,
    AVG(COALESCE(quantity, 0)) AS avg_treating_nulls_as_zero
FROM sales
GROUP BY product_id
ORDER BY product_id;

-- Handle NULL results in aggregates
SELECT 
    region,
    COALESCE(AVG(discount), 0) AS avg_discount,
    COALESCE(SUM(discount), 0) AS total_discount
FROM sales
GROUP BY region
ORDER BY region;

-- NULL in GROUP BY columns (NULLs group together)
-- SQL Server compatible version
SELECT 
    COALESCE(CAST(customer_id AS VARCHAR), 'Anonymous') AS customer,
    COUNT(*) AS purchase_count,
    SUM(quantity * unit_price) AS total_spent
FROM sales
GROUP BY customer_id
ORDER BY customer_id;

-- ----------------------------------------------------------------------------
-- SECTION 7: Common Pitfalls and Solutions
-- ----------------------------------------------------------------------------

-- PITFALL 1: Trying to nest aggregates
-- INCORRECT:
/*
SELECT region, MAX(AVG(quantity))
FROM sales
GROUP BY region;
-- ERROR: Cannot nest aggregate functions
*/

-- CORRECT: Use subquery (SQL Server compatible)
SELECT MAX(avg_quantity) AS max_avg_quantity
FROM (
    SELECT region, AVG(quantity) AS avg_quantity
    FROM sales
    GROUP BY region
) AS regional_averages;

-- PITFALL 2: Referencing alias in WHERE (not allowed)
-- INCORRECT:
/*
SELECT 
    product_id,
    COUNT(*) AS sales_count
FROM sales
WHERE sales_count > 2  -- ERROR: Cannot use alias in WHERE
GROUP BY product_id;
*/

-- CORRECT: Use HAVING instead
SELECT 
    product_id,
    COUNT(*) AS sales_count
FROM sales
GROUP BY product_id
HAVING COUNT(*) > 2;

-- PITFALL 3: Division by zero in aggregate calculations
-- INCORRECT: Can cause division by zero
/*
SELECT 
    region,
    SUM(quantity * unit_price) / COUNT(customer_id) AS revenue_per_customer
FROM sales
GROUP BY region;
-- Error if COUNT(customer_id) = 0 for any region
*/

-- CORRECT: Use NULLIF or CASE
SELECT 
    region,
    SUM(quantity * unit_price) / NULLIF(COUNT(customer_id), 0) AS revenue_per_customer
FROM sales
GROUP BY region;

-- Or using CASE
SELECT 
    region,
    CASE 
        WHEN COUNT(customer_id) > 0 
        THEN SUM(quantity * unit_price) / COUNT(customer_id)
        ELSE 0
    END AS revenue_per_customer
FROM sales
GROUP BY region;

-- PITFALL 4: Not understanding empty groups
-- Empty table with GROUP BY returns no rows
CREATE TABLE empty_sales (
    product_id INT,
    quantity INT
);

SELECT product_id, SUM(quantity) AS total
FROM empty_sales
GROUP BY product_id;
-- Returns: 0 rows (not a single row with NULL)

-- Without GROUP BY, returns one row with NULLs
SELECT SUM(quantity) AS total
FROM empty_sales;
-- Returns: 1 row with NULL

-- ----------------------------------------------------------------------------
-- SECTION 8: DISTINCT in Aggregation
-- ----------------------------------------------------------------------------

-- DISTINCT with COUNT
SELECT 
    COUNT(*) AS total_sales,
    COUNT(DISTINCT customer_id) AS unique_customers,
    COUNT(DISTINCT product_id) AS unique_products,
    COUNT(DISTINCT region) AS unique_regions
FROM sales;

-- DISTINCT in other aggregates
SELECT 
    region,
    COUNT(*) AS total_sales,
    COUNT(DISTINCT product_id) AS unique_products,
    SUM(quantity) AS total_quantity,
    SUM(DISTINCT quantity) AS sum_of_distinct_quantities,
    AVG(unit_price) AS avg_price,
    AVG(DISTINCT unit_price) AS avg_of_distinct_prices
FROM sales
GROUP BY region
ORDER BY region;

-- Practical use case: Customer analytics
SELECT 
    customer_id,
    COUNT(*) AS total_purchases,
    COUNT(DISTINCT product_id) AS unique_products_bought,
    COUNT(DISTINCT region) AS regions_purchased_from,
    SUM(quantity * unit_price) AS total_spent,
    AVG(quantity * unit_price) AS avg_order_value
FROM sales
WHERE customer_id IS NOT NULL
GROUP BY customer_id
ORDER BY total_spent DESC;

-- ----------------------------------------------------------------------------
-- SECTION 9: Advanced GROUP BY Techniques
-- ----------------------------------------------------------------------------

-- ROLLUP: Generate subtotals and grand totals (SQL Server compatible)
SELECT 
    region,
    product_id,
    SUM(quantity * unit_price) AS total_revenue
FROM sales
GROUP BY ROLLUP(region, product_id)
ORDER BY region, product_id;

-- CUBE: Generate all possible combinations of subtotals (SQL Server compatible)
SELECT 
    region,
    product_id,
    SUM(quantity * unit_price) AS total_revenue
FROM sales
GROUP BY CUBE(region, product_id)
ORDER BY region, product_id;

-- GROUPING SETS: Specify exactly which groupings you want (SQL Server compatible)
SELECT 
    region,
    product_id,
    SUM(quantity * unit_price) AS total_revenue
FROM sales
GROUP BY GROUPING SETS (
    (region),
    (product_id),
    (region, product_id),
    ()  -- Grand total
)
ORDER BY region, product_id;

-- SQL Server alternative for FILTER clause (using CASE)
SELECT 
    region,
    COUNT(*) AS total_sales,
    SUM(CASE WHEN quantity > 5 THEN 1 ELSE 0 END) AS large_sales,
    AVG(quantity) AS avg_quantity,
    AVG(CASE WHEN discount IS NOT NULL THEN quantity ELSE NULL END) AS avg_qty_with_discount
FROM sales
GROUP BY region
ORDER BY region;

-- ----------------------------------------------------------------------------
-- SECTION 10: Practical Business Examples
-- ----------------------------------------------------------------------------

-- Example 1: Sales performance by region and category
SELECT 
    s.region,
    p.category,
    COUNT(*) AS num_sales,
    SUM(s.quantity) AS total_units_sold,
    SUM(s.quantity * s.unit_price) AS gross_revenue,
    SUM(COALESCE(s.discount, 0)) AS total_discounts,
    SUM(s.quantity * s.unit_price) - SUM(COALESCE(s.discount, 0)) AS net_revenue,
    AVG(s.quantity * s.unit_price) AS avg_order_value
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY s.region, p.category
HAVING SUM(s.quantity * s.unit_price) > 500
ORDER BY net_revenue DESC;

-- Example 2: Customer purchase patterns
SELECT 
    c.customer_name,
    COUNT(*) AS total_purchases,
    COUNT(DISTINCT s.product_id) AS unique_products,
    SUM(s.quantity) AS total_items,
    SUM(s.quantity * s.unit_price) AS total_spent,
    AVG(s.quantity * s.unit_price) AS avg_purchase,
    MIN(s.sale_date) AS first_purchase,
    MAX(s.sale_date) AS last_purchase
FROM customers c
LEFT JOIN sales s ON c.customer_id = s.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spent DESC;

-- Example 3: Product performance analysis
SELECT 
    p.product_name,
    p.category,
    COUNT(s.sale_id) AS times_sold,
    COALESCE(SUM(s.quantity), 0) AS total_units_sold,
    COALESCE(SUM(s.quantity * s.unit_price), 0) AS total_revenue,
    COALESCE(AVG(s.quantity * s.unit_price), 0) AS avg_sale_value,
    COUNT(DISTINCT s.customer_id) AS unique_customers
FROM products p
LEFT JOIN sales s ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_revenue DESC;

-- Example 4: Time-based analysis (SQL Server compatible)
SELECT 
    CAST(sale_date AS DATE) AS sale_day,
    COUNT(*) AS daily_sales,
    SUM(quantity) AS daily_units,
    SUM(quantity * unit_price) AS daily_revenue,
    COUNT(DISTINCT customer_id) AS unique_customers,
    AVG(quantity * unit_price) AS avg_order_value
FROM sales
GROUP BY CAST(sale_date AS DATE)
ORDER BY sale_day;

-- ----------------------------------------------------------------------------
-- SECTION 11: Performance Tips
-- ----------------------------------------------------------------------------

-- Use indexes on columns frequently used in GROUP BY
CREATE INDEX idx_sales_region ON sales(region);
CREATE INDEX idx_sales_product_id ON sales(product_id);
CREATE INDEX idx_sales_customer_id ON sales(customer_id);
CREATE INDEX idx_sales_date ON sales(sale_date);

-- Composite index for common GROUP BY combinations
CREATE INDEX idx_sales_region_product ON sales(region, product_id);

-- View execution plan (SQL Server)
SET SHOWPLAN_ALL ON;
GO
SELECT 
    region,
    product_id,
    COUNT(*) AS sales_count,
    SUM(quantity * unit_price) AS revenue
FROM sales
GROUP BY region, product_id;
GO
SET SHOWPLAN_ALL OFF;
GO

-- Alternative: Use graphical execution plan
-- Press Ctrl+L in SQL Server Management Studio before running query

-- Pre-aggregate in indexed views for frequently accessed summaries
-- Note: Indexed views require SCHEMABINDING and specific conditions
CREATE VIEW v_regional_sales
WITH SCHEMABINDING
AS
SELECT 
    s.region,
    s.product_id,
    COUNT_BIG(*) AS sales_count,
    SUM(s.quantity) AS total_quantity,
    SUM(s.quantity * s.unit_price) AS total_revenue
FROM dbo.sales s
GROUP BY s.region, s.product_id;
GO

-- Create index on the view
CREATE UNIQUE CLUSTERED INDEX idx_v_regional_sales 
ON v_regional_sales(region, product_id);
GO

-- Query the indexed view (SQL Server will use it automatically)
SELECT * FROM v_regional_sales
WHERE region = 'North'
ORDER BY total_revenue DESC;

-- ----------------------------------------------------------------------------
-- CLEANUP
-- ----------------------------------------------------------------------------

DROP VIEW IF EXISTS v_regional_sales;
DROP INDEX IF EXISTS idx_sales_region ON sales;
DROP INDEX IF EXISTS idx_sales_product_id ON sales;
DROP INDEX IF EXISTS idx_sales_customer_id ON sales;
DROP INDEX IF EXISTS idx_sales_date ON sales;
DROP INDEX IF EXISTS idx_sales_region_product ON sales;

DROP TABLE IF EXISTS test_nulls;
DROP TABLE IF EXISTS all_nulls;
DROP TABLE IF EXISTS empty_sales;
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

-- ============================================================================
-- END OF Q6 EXAMPLES
-- ============================================================================