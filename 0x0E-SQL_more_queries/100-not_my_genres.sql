-- Listing all genres related to the tv show Dexter

SELECT gnr.name
       FROM tv_genres AS gnr
       INNER JOIN tv_show_genres AS tsg
       ON gnr.id = tsg.genre_id
       INNER JOIN tv_shows AS ts
       ON tsg.show_id = ts.id
       WHERE g.name NOT IN (
       	      (SELECT `name`
                FROM `tv_genres` AS g
	             INNER JOIN `tv_show_genres` AS s
		     ON g.`id` = s.`genre_id`

		     INNER JOIN `tv_shows` AS t
		     ON s.`show_id` = t.`id`
		     WHERE t.`title` = "Dexter")
 ORDER BY g.`name`;
