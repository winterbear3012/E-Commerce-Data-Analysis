SELECT 
    SUM(payment_value) AS total_revenue
FROM order_payments;

SELECT COUNT(*) AS total_orders
FROM orders;

SELECT 
    ROUND(SUM(payment_value) / COUNT(DISTINCT order_id), 2) AS average_order_value
FROM order_payments;

SELECT
    order_status,
    COUNT(*) AS order_count
FROM orders
GROUP BY order_status
ORDER BY order_count DESC;

SELECT
    o.order_status,
    ROUND(SUM(op.payment_value), 2) AS revenue
FROM orders o
JOIN order_payments op
    ON o.order_id = op.order_id
GROUP BY o.order_status
ORDER BY revenue DESC;

SELECT
    DATE_TRUNC('month', o.order_purchase_timestamp) AS month,
    ROUND(SUM(op.payment_value), 2) AS revenue
FROM orders o
JOIN order_payments op
    ON o.order_id = op.order_id
GROUP BY month
ORDER BY month;

SELECT
    COALESCE(pct.product_category_name_english, p.product_category_name) AS category,
    ROUND(SUM(oi.price), 2) AS revenue
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
LEFT JOIN product_category_name pct
    ON p.product_category_name = pct.product_category_name
GROUP BY category
ORDER BY revenue DESC
LIMIT 10;

SELECT
    oi.seller_id,
    ROUND(SUM(oi.price), 2) AS revenue
FROM order_items oi
GROUP BY oi.seller_id
ORDER BY revenue DESC
LIMIT 10;
SELECT
    payment_type,
    COUNT(*) AS payment_count,
    ROUND(SUM(payment_value), 2) AS total_payment
FROM order_payments
GROUP BY payment_type
ORDER BY total_payment DESC;
SELECT
    review_score,
    COUNT(*) AS review_count
FROM order_reviews
GROUP BY review_score
ORDER BY review_score;

SELECT
    ROUND(AVG(review_score), 2) AS average_review_score
FROM order_reviews;

SELECT
    ROUND(
        AVG(
            EXTRACT(EPOCH FROM (
                order_deliverd_customer_date - order_purches_timestamp
            )) / 86400
        ), 2
    ) AS average_delivery_days
FROM orders
WHERE order_deliverd_customer_date IS NOT NULL;

SELECT
    ROUND(AVG(freight_value), 2) AS average_freight_value,
    ROUND(SUM(freight_value), 2) AS total_freight_value
FROM order_items;

SELECT
    c.customer_state,
    ROUND(SUM(op.payment_value), 2) AS revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_payments op
    ON o.order_id = op.order_id
GROUP BY c.customer_state
ORDER BY revenue DESC;

SELECT
    c.customer_city,
    ROUND(SUM(op.payment_value), 2) AS revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_payments op
    ON o.order_id = op.order_id
GROUP BY c.customer_city
ORDER BY revenue DESC
LIMIT 10;

SELECT
    c.customer_state,
    COUNT(DISTINCT o.order_id) AS order_count
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_state
ORDER BY order_count DESC;