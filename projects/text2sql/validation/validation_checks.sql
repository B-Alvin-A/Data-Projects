-- Revenue Consistency
-- Total revenue from order_items
SELECT SUM(quantity * unit_price) FROM order_items;

-- Should match:
SELECT SUM(monthly_revenue)
FROM (
    SELECT DATE_TRUNC('month', o.order_date) AS month,
           SUM(oi.quantity * oi.unit_price) AS monthly_revenue
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    GROUP BY month
) t;

-- Order Count Consistency
SELECT COUNT(*) FROM orders;

SELECT SUM(order_count)
FROM (
    SELECT COUNT(*) AS order_count
    FROM orders
    GROUP BY customer_id
) t;

-- No Negative Revenue
SELECT *
FROM order_items
WHERE quantity * unit_price < 0;

-- Status Integrity
SELECT DISTINCT status FROM orders;

-- Duplicate Detection
SELECT order_id, product_id, COUNT(*)
FROM order_items
GROUP BY order_id, product_id
HAVING COUNT(*) > 1;