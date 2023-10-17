-- Displays the max temperature of each state

select state, MAX(values) as max_temp
FROM  temperatures
GROUP BY state
ORDER BY max_temp DESC
