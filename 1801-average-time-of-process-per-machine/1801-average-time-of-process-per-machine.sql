# Write your MySQL query statement below

SELECT t1.machine_id,
ROUND(AVG(t2.timestamp - t1.timestamp), 3) AS processing_time
FROM 
Activity as t1,
Activity as t2
WHERE t1.activity_type = 'start'
AND
t2.activity_type = 'end'
AND
t1.process_id = t2.process_id
AND
t1.machine_id = t2.machine_id

GROUP BY machine_id;
