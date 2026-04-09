CREATE TABLE stg_orders AS
SELECT
    order_id,
    customer_id,
    order_status,

    CAST(order_purchase_timestamp AS TIMESTAMP) AS order_purchase_ts,
    CAST(order_approved_at AS TIMESTAMP) AS order_approved_ts,
    CAST(order_delivered_carrier_date AS TIMESTAMP) AS order_delivered_carrier_ts,
    CAST(order_delivered_customer_date AS TIMESTAMP) AS order_delivered_customer_ts,
    CAST(order_estimated_delivery_date AS TIMESTAMP) AS order_estimated_delivery_ts

FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY ingested_at DESC) AS rn
    FROM raw_orders
    WHERE order_id IS NOT NULL
) t
WHERE rn = 1;