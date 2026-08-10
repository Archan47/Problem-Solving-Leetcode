# Write your MySQL query statement below
SELECT t1.person_name
FROM Queue t1
INNER JOIN Queue t2
ON t1.turn >= t2.turn
GROUP BY t1.turn
HAVING SUM(t2.weight) <= 1000
ORDER BY SUM(t2.weight) DESC
LIMIT 1;