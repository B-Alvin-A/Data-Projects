CREATE TABLE stg_payments AS
SELECT
    order_id,
    payment_sequential,
    payment_type,

    CAST(payment_installments AS INTEGER) AS payment_installments,
    CAST(payment_value AS NUMERIC(10,2)) AS payment_value

FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY order_id, payment_sequential
               ORDER BY ingested_at DESC
           ) AS rn
    FROM raw_payments
    WHERE order_id IS NOT NULL
) t
WHERE rn = 1;