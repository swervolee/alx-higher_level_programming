-- Prints all cities in th database in the format
--- city_id citie_name states_name

SELECT `cities`.`id`, `cities`.`name`, `states`.`name`
       FROM `cities`
       INNER JOIN `states`
       on `cities`.`state_id` = `states`.`id`
       ORDER BY `cities`.`id` ASC
