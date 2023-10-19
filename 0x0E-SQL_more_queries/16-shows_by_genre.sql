-- script that lists all shows of a genre

SELECT tvs.title, tvg.name
FROM (tv_shows tvs
	LEFT JOIN tv_show_genres tvsg
	ON tvs.id = tvsg.show_id
) LEFT JOIN tv_genres tvg
ON tvsg.genre_id = tvg.id
ORDER BY tvs.title, tvg.name;
