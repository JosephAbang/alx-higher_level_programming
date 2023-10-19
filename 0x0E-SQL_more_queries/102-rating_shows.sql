-- script that lists all shows from hbtn_0d_tvshows_rate by their rating


SELECT tvs.title, SUM(rate) rating
FROM tv_shows tvs
INNER JOIN tv_show_ratings
ON id = show_id
GROUP BY title
ORDER BY rating DESC;
