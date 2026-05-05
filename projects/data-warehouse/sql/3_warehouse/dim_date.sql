-- dim_date
CREATE TABLE dim_date AS
WITH date_series AS (
    SELECT generate_series(
        (SELECT MIN(order_purchase_ts)::date FROM stg_orders),
        (SELECT MAX(order_purchase_ts)::date FROM stg_orders),
        interval '1 day'
    )::date AS full_date
)
SELECT
    ROW_NUMBER() OVER (ORDER BY full_date) AS date_sk,
    full_date,

    EXTRACT(YEAR FROM full_date) AS year,
    EXTRACT(MONTH FROM full_date) AS month,
    EXTRACT(DAY FROM full_date) AS day,

    EXTRACT(QUARTER FROM full_date) AS quarter,
    TO_CHAR(full_date, 'Day') AS day_name,
    TO_CHAR(full_date, 'Month') AS month_name,

    EXTRACT(DOW FROM full_date) AS day_of_week

FROM date_series;