-- script that lists all genres of a show

SELECT tvg.name
FROM (tv_shows tvs
	INNER JOIN tv_show_genres tvsg
	ON tvs.id = tvsg.show_id
) INNER JOIN tv_genres tvg
ON tvsg.genre_id = tvg.id
WHERE tvs.title = 'Dexter'
GROUP BY tvg.name
ORDER BY tvg.name;
