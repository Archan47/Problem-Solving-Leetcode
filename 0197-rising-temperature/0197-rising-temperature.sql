# Write your MySQL query statement below
SELECT today.id
FROM Weather AS today
WHERE EXISTS (
    SELECT 1
    FROM Weather AS yesterday
    WHERE today.recordDate = DATE_ADD(yesterday.recordDate, INTERVAL 1 DAY)
      AND today.temperature > yesterday.temperature
);