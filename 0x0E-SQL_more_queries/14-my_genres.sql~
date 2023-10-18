-- Listing all the genres of the show dexter

SELECT gnr.name
       FROM tv_genres AS gnr
       INNER JOIN tv_show_genres AS tsg
       	     ON gnr.id = tsg.genre_id
       INNER JOIN tv_shows as ts
       	     ON  tsg.show_id = ts.id
	WHERE ts.title = "Dexter"
	ORDER BY gnr.name
