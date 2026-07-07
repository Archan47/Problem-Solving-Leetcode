# Write your MySQL query statement below
select s.name from salesperson s
WHERE sales_id not in (
select o.sales_id from orders o
INNER JOIN company c
ON o.com_id = c.com_id
WHERE c.name = 'RED'
);
