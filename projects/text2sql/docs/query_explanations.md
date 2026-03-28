# 📊 SQL Query Explanations & Performance Insights

This document explains the purpose, execution behavior, and optimization considerations for analytical queries run on the sales database.

---

## 1. 💰 Total Revenue Generated

```sql
SELECT 
SUM(quantity * unit_price) AS "Total Revenue"
FROM order_items;
```

### 📌 Purpose

Calculates total revenue across all orders.

### ⚙️ Execution Behavior

* Performs a **sequential scan** on `order_items`
* Applies aggregation (`SUM`) across all rows

### 🚫 Index Usage

* Indexes are **not used**
* Entire table must be scanned → index provides no benefit

### 🧠 Takeaway

> Aggregation over entire tables is **I/O bound**, not lookup bound.

---

## 2. 🌍 Orders per Region

```sql
SELECT 
    c.region,
    COUNT(*)
FROM orders o
JOIN customers c
on o.customer_id = c.customer_id
GROUP BY c.region;
```

### 📌 Purpose

Counts how many orders were placed in each region.

### ⚙️ Execution Behavior

* Sequential scans on both tables
* **Hash Join** on `customer_id`
* Aggregation by `region`

### 🚫 Index Usage

* Not used because:

  * No filtering
  * Most rows are processed

### 🧠 Takeaway

> Joins + aggregation over full datasets favor **hash joins + seq scans**

---

## 3. 🏆 Top 5 Customers by Spend

```sql
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
```

### 📌 Purpose

Identifies highest-value customers.

### ⚙️ Execution Behavior

* Sequential scans across all tables
* Hash joins
* Aggregation per customer
* **Top-N sort**

### 🚫 Index Usage

* Ignored because:

  * Full aggregation required
  * No filtering

### 🚀 Optimization Insight

* Pre-aggregate using orders + order_items first
* Join customers later

### 🧠 Takeaway

> Indexes don’t help when **all rows must be aggregated**

---

## 4. 📅 Monthly Revenue Trend

```sql
SELECT
    DATE_TRUNC('month', o.order_date) AS month,
    SUM(oi.quantity * oi.unit_price) AS "Monthly Revenue"
FROM orders o JOIN order_items oi
ON o.order_id = oi.order_id
GROUP BY month
ORDER BY month;
```

### 📌 Purpose

Tracks revenue trends over time.

### ⚙️ Execution Behavior

* Join + aggregation
* Sorting by month

### 🚫 Index Usage

* Not used because:

  * Grouping transforms data
  * Requires full scan

### 🧠 Takeaway

> Time-based aggregations typically require **full data processing**

---

## 5. 📦 Average Order Value

```sql
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
```

### 📌 Purpose

Calculates average revenue per order.

### ⚙️ Execution Behavior

* First aggregation: per order
* Second aggregation: average

### 🚫 Index Usage

* Not helpful due to:

  * Full aggregation requirement

### 🧠 Takeaway

> Multi-level aggregations are **compute-heavy operations**

---

## 6. 📈 Cumulative Revenue (Window Function)

### Version 1 (Nested SUM)

```sql
SELECT
    o.order_date,
    SUM(oi.quantity * oi.unit_price) AS daily_revenue,
    SUM(SUM(oi.quantity * oi.unit_price)) OVER (
        ORDER BY o.order_date
    ) AS cumulative_revenue
FROM orders o JOIN order_items oi 
ON o.order_id = oi.order_id
WHERE o.status = 'completed'
GROUP BY o.order_date
ORDER BY o.order_date;
```

### Version 2 (Optimized)

```sql
WITH daily_revenue AS (
    SELECT
        o.order_date,
        SUM(oi.quantity * oi.unit_price) AS revenue
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.status = 'completed'
    GROUP BY o.order_date
)
SELECT
    order_date,
    revenue,
    SUM(revenue) OVER (ORDER BY order_date) AS cumulative_revenue
FROM daily_revenue;
```

### 📌 Purpose

Tracks revenue accumulation over time.

### ⚙️ Execution Behavior

* Aggregation → Sort → Window function

### 🚫 Index Usage

* Not used because:

  * Data must be grouped + sorted

### 🚀 Optimization Insight

> Pre-aggregation (Version 2) improves clarity and performance

---

## 7. 📊 Month-to-Month Revenue Growth (LAG)

```sql
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', o.order_date) AS month,
        SUM(oi.quantity * oi.unit_price) AS revenue
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.status = 'completed'
    GROUP BY month
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
FROM revenue_with_lag;
```

### 📌 Purpose

Measures revenue growth trends.

### ⚙️ Execution Behavior

* Aggregation → Sort → Window function (`LAG`)

### 🧠 Takeaway

> Window functions require **ordered datasets**, forcing sort operations

---

## 8. 🛍 Best-Selling Product per Category

```sql
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
```

### 📌 Purpose

Finds top-performing product per category.

### ⚙️ Execution Behavior

* Aggregation
* Partitioned ranking using window function

### 🧠 Takeaway

> Ranking queries are **CPU-heavy due to sorting within partitions**

---

## 9. 👥 Orders per Customer

```sql
SELECT
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS total_orders
FROM customers c LEFT JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_orders DESC;
```

### 📌 Purpose

Counts number of orders per customer.

### ⚙️ Execution Behavior

* LEFT JOIN ensures all customers included
* Aggregation + sorting

### 🧠 Takeaway

> Simple aggregations still require full scans when no filters exist

---

## 10. 📉 Customers Spending Less Over Time

```sql
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
```

### 📌 Purpose

Identifies customers whose spending is declining.

### ⚙️ Execution Behavior

* Aggregation → Sort → Window function → Filter

### 🚫 Index Usage

* Not used due to:

  * Full aggregation
  * Window function ordering

### 🧠 Takeaway

> Analytical queries combining **aggregation + window functions** are dominated by computation, not indexing

---

# 🔥 Final Insights

### ✅ When indexes help

* Selective filters (`WHERE`)
* Large datasets (millions of rows)
* Lookup-heavy queries

### ❌ When indexes don’t help

* Full-table aggregations
* Window functions
* Broad joins without filters

---

## 🧠 Core Principle

> **Indexes help you find data.
> They do not help you process all of it.**

---

## 🚀 Recommended Improvements for Scale

* Use **materialized views** for repeated analytics
* Pre-aggregate data before applying window functions
* Use **partial indexes** for filtered queries (e.g., `status = 'completed'`)
* Consider data partitioning for large time-series datasets

---

📌 *This project demonstrates real-world analytical SQL patterns and highlights how query design impacts performance more than indexing in aggregation-heavy workloads.*

---
