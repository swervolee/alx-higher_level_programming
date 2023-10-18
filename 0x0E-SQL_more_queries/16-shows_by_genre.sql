-- Lists all shows and all genres linked to that show

SELECT ts.title, gnr.name
       FROM tv_genres AS gnr
       LEFT JOIN tv_show_genres AS tsg
       	     ON gnr.id = tsg.genre_id
	LEFT JOIN tv_shows AS ts
	     ON tsg.show_id = ts.id
	ORDER BY ts.title, genre.name
