-- script that uses the hbtn_0d_tvshows database to 
-- list all genres not linked to the show Dexter

SELECT DISTINCT(tvg.name)
FROM tv_genres tvg
INNER JOIN tv_show_genres tvsg
ON tvg.id = tvsg.genre_id
INNER JOIN tv_shows AS tv
ON tvsg.show_id = tv.id
WHERE tvg.id NOT IN (
	SELECT tvsg.genre_id
	FROM tv_shows tvs
	INNER JOIN tv_show_genres tvsg
	ON tvs.id = tvsg.show_id
	WHERE tvs.title = 'Dexter'
)
ORDER BY tvg.name;
