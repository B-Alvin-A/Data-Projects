-- What is the total revenue generated?
SELECT 
SUM(quantity * unit_price) AS "Total Revenue"
FROM order_items;

-- How many orders were placed in each region?
SELECT 
    c.region,
    COUNT(*)
FROM orders o
JOIN customers c
on o.customer_id = c.customer_id
GROUP BY c.region;

-- Who are the top 5 customers by total spending?
SELECT 
    c.customer_id,
    c.name,
    SUM(oi.quantity*oi.unit_price) AS "Total Customer Spend"
FROM customers c 
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY c.customer_id
ORDER BY "Total Customer Spend" DESC
LIMIT 5;

-- What is the monthly revenue trend?
SELECT
    DATE_TRUNC('month', o.order_date) AS month,
    SUM(oi.quantity * oi.unit_price) AS "Monthly Revenue"
FROM orders o JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY month
ORDER BY month;

-- What is the average value per order?

WITH totalSales AS (
    SELECT 
        o.order_id,
        SUM(quantity*unit_price) AS "Total Order Value"
    FROM orders o JOIN order_items oi 
    ON o.order_id = oi.order_id
    GROUP BY o.order_id
)
SELECT AVG("Total Order Value") AS "Avg order Value" 
FROM totalSales;