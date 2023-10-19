-- Listing all genres related to the tv show Dexter

SELECT gnr.name
       FROM tv_genres AS gnr
       INNER JOIN tv_show_genres AS tsg
       ON gnr.id = tsg.genre_id
       INNER JOIN tv_shows AS ts
       ON tsg.show_id = ts.id
       WHERE g.name NOT IN (
       	     SELECT ts.title
	     	    FROM tv_shows AS ts
		    INNER JOIN tv_show_genres AS tsg
		    ON ts.id = tsg.show_id
		    INNER JOIN tv_genre AS gnr
		    ON tsg.genre_id = gnr.id
		    WHERE ts.title = "Dexter"
		    )
	ORDER BY gnr.name
