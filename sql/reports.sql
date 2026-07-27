-- count of tables

SELECT COUNT(*) FROM dim_customer;
SELECT COUNT(*) FROM dim_product;
SELECT COUNT(*) FROM dim_channel;
SELECT COUNT(*) FROM dim_date;
SELECT COUNT(*) FROM fact_sales;

-- max and mim sale date

SELECT MIN(sale_date), MAX(sale_date)
FROM fact_sales;

-- checking nulls

SELECT COUNT(*) FROM fact_sales
WHERE customer_id IS NULL;

SELECT COUNT(*) FROM fact_sales
WHERE product_id IS NULL;

-- show dim_customer, dim_product and dim_channel

SELECT * FROM dim_customer LIMIT 10;
SELECT * FROM dim_customer LIMIT 10;
SELECT * FROM dim_channel;

SELECT COUNT(*) FROM fact_sales
LEFT JOIN dim_customer ON fact_sales.customer_id = dim_customer.customer_id
WHERE dim_customer.customer_id IS NULL;

SELECT COUNT(*) FROM fact_sales
LEFT JOIN dim_product ON fact_sales.product_id = dim_product.product_id
WHERE dim_product.product_id IS NULL;