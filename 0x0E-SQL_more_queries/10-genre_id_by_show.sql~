-- Imports a tv show database
-- Lists all the shows by order of tvshow title and tvshow genre id

SELECT tv_shows.title, tv_show_genres.genre_id
       FROM hbtn_0d_tvshows
       INNER JOIN tv_show_genres
       	     ON tv_shows.id = tv_show_genres.genre_id
       ORDER BY tv_shows.title, tv_show_genres.genre_id
