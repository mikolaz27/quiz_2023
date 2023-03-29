SELECT customers.customer_name, orders.order_date, SUM(order_details.unit_price * order_details.quantity) as total_sales
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
JOIN order_details ON orders.order_id = order_details.order_id
WHERE customers.country IN (
    SELECT countries.country_name
    FROM countries
    JOIN regions ON countries.region_id = regions.region_id
    WHERE regions.region_name = 'North America'
)
GROUP BY customers.customer_name, orders.order_date
HAVING total_sales > (
    SELECT AVG(total_sales)
    FROM (
        SELECT customers.customer_name, SUM(order_details.unit_price * order_details.quantity) as total_sales
        FROM customers
        JOIN orders ON customers.customer_id = orders.customer_id
        JOIN order_details ON orders.order_id = order_details.order_id
        GROUP BY customers.customer_name
    ) as customer_sales
)
ORDER BY total_sales DESC;

select * from test_view;