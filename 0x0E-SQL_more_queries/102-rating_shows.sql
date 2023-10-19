-- script that lists all shows from hbtn_0d_tvshows_rate by their rating


SELECT title, SUM(rate) rating
FROM tv_shows
INNER JOIN tv_shows_ratings
ON id = show_id
GROUP BY title
ORDER BY rating DESC;
