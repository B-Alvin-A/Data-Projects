CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    region TEXT,
    signup_date DATE
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    price NUMERIC(10,2) CHECK (price >= 0)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    status TEXT CHECK (status IN ('pending', 'completed', 'cancelled')),

    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON DELETE CASCADE
);

CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT CHECK (quantity > 0),
    unit_price NUMERIC(10,2) CHECK (unit_price >= 0),

    CONSTRAINT fk_order_items_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_order_items_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
        ON DELETE RESTRICT
);


SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';

SELECT conname, contype
FROM pg_constraint;


-- DROP TABLE order_items, orders, products, customers CASCADE;

-- Data Validity Checks

SELECT COUNT(*) FROM customers; 200
SELECT COUNT(*) FROM orders; 300
SELECT COUNT(*) FROM order_items; 912

SELECT *
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL; 

SELECT *
FROM order_items oi
LEFT JOIN orders o ON oi.order_id = o.order_id
WHERE o.order_id IS NULL;

SELECT SUM(quantity * unit_price) AS total_revenue
FROM order_items;

SELECT status, COUNT(*)
FROM orders
GROUP BY status;

SELECT MIN(order_date), MAX(order_date)
FROM orders;