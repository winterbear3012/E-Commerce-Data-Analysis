CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_unique_id VARCHAR(50),
    customer_zip_code_prefix INT,
    customer_city VARCHAR(100),
    customer_state VARCHAR(10)
);

CREATE TABLE geolocation(
    geolocation_zipcode_prefix INT,
    geolocation_len DECIMAL(10,7),
    geolocation_lag DECIMAL(10,7),
    geolocation_city VARCHAR(100),
    geolocation_state VARCHAR(10)
);

CREATE TABLE orders(
    order_id VARCHAR(40), PRIMARY KEY,
    customer_id VARCHAR(50) REFERENCES customers(customer_id),
    order_status VARCHAR(30),
    order_purches_timestamp TIMESTAMP,
    order_approvved_at TIMESTAMP,
    order_deliverd_carrier_date TIMESTAMP,
    order_deliverd_customer_date TIMESTAMP,
    order_estimate_delivery_date TIMESTAMP
);

CREATE TABLE order_items (
    order_id VARCHAR(50), REFERENCES orders(order_id)
    order_item_id INT,
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    shipping_limit_date TIMESTAMP,
    price DECIMAL(10,2),
    freight_value DECIMAL(10,2),
    PRIMARY KEY (order_id,order_item_id)
);

CREATE TABLE order_payments (
    order_id VARCHAR(50) REFERENCES orders(order_id),
    payment_sequntial INT,
    payment_type VARCHAR(30),
    payment_installation INT,
    payment_value DECIMAL(10,2),
    PRIMARY KEY (order_id, payment_sequntial)
);

CREATE TABLE order_reviews (
    review_id VARCHAR(50) PRIMARY KEY,
    order_id VARCHAR(50)  REFERENCES orders(order_id),
    review_score INT,
    review_comment_title Text,
    review_comment_message Text,
    review_creation_date TIMESTAMP,
    review_answer_timestamp TIMESTAMP
);

CREATE TABLE products (
    product_id VARCHAR (50) PRIMARY KEY,
    product_category_name VARCHAR(100),
    product_name_length DECIMAL(10,2),
    product_description_length DECIMAL(10,2),
    product_photo_qty DECIMAL(10,2),
    product_weigth_g DECIMAL(10,2),
    product_length_cm DECIMAL(10,2),
    product_height_cm DECIMAL(10,2),
    product_width_cm DECIMAL(10,2)
);

CREATE TABLE sellers (
    seller_id VARCHAR(50) PRIMARY KEY,
    seller_zipcode_prefix INT,
    seller_city VARCHAR(100),
    seller_state VARCHAR(10)
);


CREATE TABLE product_category_name (
    product_category_name VARCHAR(100) PRIMARY KEY,
    product_category_name_english VARCHAR(100)
);
