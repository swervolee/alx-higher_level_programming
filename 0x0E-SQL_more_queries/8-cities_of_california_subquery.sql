-- Selects cities that can be found in california state in hbtn_0d_usa database.

SELECT `id`, `name`
       FROM `cities`
       WHERE `state_id` IN (
       	     select `id`
       	     FROM `states`
       	     where `name` = 'california')
      ORDER BY `id`
