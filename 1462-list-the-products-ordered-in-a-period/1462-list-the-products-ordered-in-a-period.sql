# Write your MySQL query statement below
SELECT t1.product_name, SUM(t2.unit) AS unit
FROM Products t1
JOIN Orders t2
ON t1.product_id = t2.product_id
WHERE t2.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY t1.product_name
HAVING SUM(t2.unit) >= 100;