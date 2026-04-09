CREATE TABLE stg_products AS
SELECT
    product_id,

    product_category_name,

    CAST(product_weight_g AS NUMERIC) AS product_weight_g,
    CAST(product_length_cm AS NUMERIC) AS product_length_cm,
    CAST(product_height_cm AS NUMERIC) AS product_height_cm,
    CAST(product_width_cm AS NUMERIC) AS product_width_cm

FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY product_id
               ORDER BY ingested_at DESC
           ) AS rn
    FROM raw_products
    WHERE product_id IS NOT NULL
) t
WHERE rn = 1;