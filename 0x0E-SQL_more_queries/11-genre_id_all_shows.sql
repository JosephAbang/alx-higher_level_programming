--  script that lists all shows contained in hbtn_0d_tvshow

SELECT tvs.title, tvsg.genre_id 
FROM tv_shows tvs
LEFT JOIN tv_show_genres tvsg
ON tvs.id = tvsg.show_id
ORDER BY tvs.title, tvsg.genre_id;
