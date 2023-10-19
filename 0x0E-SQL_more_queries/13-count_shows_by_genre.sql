-- script that lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each

SELECT tvg.name genre, COUNT(tvs.title) number_of_shows
FROM (tv_shows tvs
	INNER JOIN tv_show_genres tvsg
	ON tvs.id = tvsg.show_id
) INNER JOIN tv_genres tvg
ON tvsg.genre_id = tvg.id
GROUP BY tvg.name
ORDER BY number_of_shows DESC;
