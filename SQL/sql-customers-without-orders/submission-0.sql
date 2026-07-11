-- Write your query below

SELECT c.name
FROM customers AS c
WHERE NOT EXISTS (
    SELECT *
    FROM orders AS o
    WHERE o.customer_id = c.id
);