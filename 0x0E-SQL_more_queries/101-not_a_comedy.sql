-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT DISTINCT(tvs.title)
FROM tv_shows tvs
LEFT JOIN tv_show_genres tvsg
ON tvs.id = tvsg.show_id
LEFT JOIN tv_genres AS tvg
ON tvsg.genre_id = tvg.id
WHERE tvs.id NOT IN (
	SELECT tvsg.show_id
	FROM tv_genres tvg
	LEFT JOIN tv_show_genres tvsg
	ON tvg.id = tvsg.genre_id
	WHERE tvg.name = 'Comedy'
)
ORDER BY tvs.title;
