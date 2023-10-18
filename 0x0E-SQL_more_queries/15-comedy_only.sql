-- Lists all the comedy shows

SELECT ts.title
       FROM tv_genres AS gnr
       INNER JOIN tv_show_genres AS tsg
       	     ON gnr.id = tsg.genre_id
	INNER JOIN tv_shows AS ts
	      on tsg.show_id = ts.id
	WHERE gnr.name = Comedy
	ORDER BY ts.title
