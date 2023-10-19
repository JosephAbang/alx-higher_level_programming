-- script that lists all shows of a genre

SELECT tvs.title
FROM (tv_shows tvs
	INNER JOIN tv_show_genres tvsg
	ON tvs.id = tvsg.show_id
) INNER JOIN tv_genres tvg
ON tvsg.genre_id = tvg.id
WHERE tvg.name = 'Comedy'
ORDER BY tvs.title;
