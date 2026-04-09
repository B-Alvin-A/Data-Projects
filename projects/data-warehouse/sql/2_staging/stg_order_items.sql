CREATE TABLE stg_order_items AS
SELECT
    order_id,
    order_item_id,
    product_id,
    seller_id,

    CAST(shipping_limit_date AS TIMESTAMP) AS shipping_limit_ts,

    CAST(price AS NUMERIC(10,2)) AS price,
    CAST(freight_value AS NUMERIC(10,2)) AS freight_value

FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY order_id, order_item_id
               ORDER BY ingested_at DESC
           ) AS rn
    FROM raw_order_items
    WHERE order_id IS NOT NULL
      AND order_item_id IS NOT NULL
) t
WHERE rn = 1;