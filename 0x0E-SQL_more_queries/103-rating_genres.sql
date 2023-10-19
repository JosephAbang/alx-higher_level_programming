-- script that lists all genres from hbtn_0d_tvshows_rate by their rating


SELECT name, SUM(rate) rating
FROM tv_shows tvs
INNER JOIN tv_show_ratings
ON tvs.id = show_id
INNER JOIN (SELECT name, tvsg.show_id
	FROM tv_show_genres tvsg
	JOIN tv_genres tvg
	ON tvsg.genre_id = tvg.id
) tvl
ON tvs.id = tvl.show_id
GROUP BY name
ORDER BY rating DESC;
