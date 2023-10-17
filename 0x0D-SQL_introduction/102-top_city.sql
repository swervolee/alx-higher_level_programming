-- Importing and using a Dump table

SELECT city, AVG(value) as avg_temp
WHERE MONTH = 7 OR MONTH = 8
GROUP BY city
ORDER BY avg_temp
LIMIT 3
