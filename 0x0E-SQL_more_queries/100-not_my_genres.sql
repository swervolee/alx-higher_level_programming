-- Listing all genres related to the tv show Dexter

SELECT gnr.name
       FROM tv_genres AS gnr
       INNER JOIN tv_show_genres as tsg
       ON gnr.id = tsg.genre_id
       INNER JOIN tv_shows AS ts
       ON tsg.show_id = ts.id
       WHERE ts.title = "Dexter"
       ORDER BY gnr.name
