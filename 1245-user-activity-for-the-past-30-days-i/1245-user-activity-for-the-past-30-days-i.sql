# Write your MySQL query statement below
SELECT DISTINCT activity_date as day,
COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE activity_date BETWEEN '2019-06-28' and '2019-07-27' 
GROUP BY activity_date;