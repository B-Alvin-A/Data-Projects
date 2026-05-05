-- dim_customer

DROP TABLE IF EXISTS dim_customer;

CREATE TABLE dim_customer AS
SELECT
    ROW_NUMBER() OVER (ORDER BY customer_unique_id) AS customer_sk,
    customer_unique_id,
    customer_city,
    customer_state
FROM (
    SELECT DISTINCT ON (customer_unique_id)
        customer_unique_id,
        customer_city,
        customer_state
    FROM stg_customers
    ORDER BY customer_unique_id, customer_id DESC
) t;