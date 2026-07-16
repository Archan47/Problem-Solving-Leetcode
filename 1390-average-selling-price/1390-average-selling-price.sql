# Write your MySQL query statement below

SELECT
    p.product_id,
    ROUND(
        IFNULL(SUM(s.units * p.price) / SUM(s.units), 0),
        2
    ) AS average_price
FROM Prices AS p
LEFT JOIN UnitsSold AS s
ON p.product_id = s.product_id
AND s.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;

