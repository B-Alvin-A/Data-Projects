CREATE TABLE stg_customers AS
SELECT
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,
    customer_city,
    customer_state

FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY customer_id
               ORDER BY ingested_at DESC
           ) AS rn
    FROM raw_customers
    WHERE customer_id IS NOT NULL
) t
WHERE rn = 1;