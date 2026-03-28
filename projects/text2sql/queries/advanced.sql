-- What is the cumulative revenue over time? Must use SUM() OVER
SELECT
    o.order_date,
    SUM(oi.quantity * oi.unit_price) AS daily_revenue,
    SUM(SUM(oi.quantity * oi.unit_price)) OVER (
        ORDER BY o.order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_revenue
FROM orders o JOIN order_items oi 
ON o.order_id = oi.order_id
WHERE o.status = 'completed'
GROUP BY o.order_date
ORDER BY o.order_date;

WITH daily_revenue AS (
    SELECT
        o.order_date,
        SUM(oi.quantity * oi.unit_price) AS revenue
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.status = 'completed'
    GROUP BY o.order_date
    ORDER BY o.order_date
)
SELECT
    order_date,
    revenue,
    SUM(revenue) OVER (ORDER BY order_date) AS cumulative_revenue
FROM daily_revenue;

-- How is revenue growing month-to-month? LAG() Revenue difference
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', o.order_date) AS month,
        SUM(oi.quantity * oi.unit_price) AS revenue
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.status = 'completed'
    GROUP BY month
    ORDER BY month
),
revenue_with_lag AS (
    SELECT
        month,
        revenue,
        LAG(revenue) OVER (ORDER BY month) AS prev_month_revenue
    FROM monthly_revenue
)
SELECT
    month,
    revenue,
    prev_month_revenue,
    revenue - prev_month_revenue AS revenue_change
FROM revenue_with_lag
ORDER BY month;

-- What is the best-selling product in each category? ROW_NUMBER() or RANK()
WITH product_sales AS (
    SELECT
        p.category,
        p.product_id,
        p.name,
        SUM(oi.quantity) AS total_sold
    FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
    JOIN orders o ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY p.category, p.product_id, p.name
),
ranked_products AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY category
            ORDER BY total_sold DESC
        ) AS rn
    FROM product_sales
)
SELECT
    category,
    product_id,
    name,
    total_sold
FROM ranked_products
WHERE rn = 1;

-- How many orders does each customer make? Simple aggregation, but must be clean
SELECT
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS total_orders
FROM customers c LEFT JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_orders DESC;

-- Which customers are spending less over time? Use LAG() or compare periods
WITH customer_monthly_spend AS (
    SELECT
        o.customer_id,
        c.name,
        DATE_TRUNC('month', o.order_date) AS month,
        SUM(oi.quantity * oi.unit_price) AS spend
    FROM customers c JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.status = 'completed'
    GROUP BY o.customer_id,c.name, month
    ORDER BY o.customer_id
),
spend_with_lag AS (
    SELECT
        *,
        LAG(spend,1,0) OVER (
            PARTITION BY customer_id
            ORDER BY month
        ) AS prev_spend
    FROM customer_monthly_spend
)
SELECT
    customer_id,
    name,
    month,
    spend,
    prev_spend,
    (spend - prev_spend) AS change
FROM spend_with_lag
WHERE prev_spend IS NOT NULL
  AND spend < prev_spend
ORDER BY customer_id, month;