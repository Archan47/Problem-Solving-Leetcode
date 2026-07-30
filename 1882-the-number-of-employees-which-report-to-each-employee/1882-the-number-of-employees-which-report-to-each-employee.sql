# Write your MySQL query statement below
SELECT
    t1.employee_id,
    t1.name,
    COUNT(*) AS reports_count,
    ROUND(AVG(t2.age)) AS average_age
FROM Employees AS t1
JOIN Employees AS t2
ON t1.employee_id = t2.reports_to
GROUP BY t1.employee_id, t1.name
ORDER BY t1.employee_id;