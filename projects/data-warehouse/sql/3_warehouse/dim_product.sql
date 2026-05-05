-- dim_product
CREATE TABLE dim_product AS
SELECT
    ROW_NUMBER() OVER (ORDER BY product_id) AS product_sk,
    product_id,
    product_category_name,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm
FROM stg_products;