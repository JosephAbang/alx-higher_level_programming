# 0x0E. SQL - More queries

Files
-----
| File Name             | Description                            |
|-----------------------|----------------------------------------|
| [0-privileges.sql](0-privileges.sql) | Lists privileges for MySQL users.   |
| [1-create_user.sql](1-create_user.sql) | Creates a new MySQL user.           |
| [2-create_read_user.sql](2-create_read_user.sql) | Creates a read-only MySQL user.   |
| [3-force_name.sql](3-force_name.sql) | Query to enforce a specific name.    |
| [4-never_empty.sql](4-never_empty.sql) | Query to make fields never empty.  |
| [5-unique_id.sql](5-unique_id.sql) | Query to enforce unique IDs.        |
| [6-states.sql](6-states.sql) | Query to list states starting with 'N'. |
| [7-cities.sql](7-cities.sql) | Query to list cities in specific states. |
| [8-cities_of_states.sql](8-cities_of_states.sql) | Query to list cities of certain states. |
| [9-cities_by_states.sql](9-cities_by_states.sql) | Query to list cities ordered by state. |
| [10-genre_id_by_show.sql](10-genre_id_by_show.sql) | Query to list show IDs by genre ID. |
| [11-genre_id_all_shows.sql](11-genre_id_all_shows.sql) | Query to list all shows and their genre. |
| [12-no_genre.sql](12-no_genre.sql) | Query to list shows without genre. |
| [13-count_shows_genre.sql](13-count_shows_genre.sql) | Query to count shows by genre. |
| [14-my_genres.sql](14-my_genres.sql) | Query to list genres of a specific user. |
| [15-only_myy_genres.sql](15-only_myy_genres.sql) | Query to list genres of a user's shows. |

Tasks
-----
**0. My privileges!**
Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

**1. Root user**
Write a script that creates the MySQL server user user_0d_1.

**2. Read user**
Write a script that creates the database hbtn_0d_2 and the user user_0d_2.

**3. Always a name**
Write a script that creates the table force_name on your MySQL server.

**4. ID can't be null**
Write a script that creates the table id_not_null on your MySQL server.

**5. Unique ID**
Write a script that creates the table unique_id on your MySQL server.

**6. States table**
Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

**7. Cities table**
Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

**8. Cities of California**
Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

**9. Cities by States**
Write a script that lists all cities contained in the database hbtn_0d_usa.

**10. Genre ID by show**
Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

**11. Genre ID for all shows**
Write a script that lists all shows contained in the database hbtn_0d_tvshows.

**12. No genre**
Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

**13. Number of shows by genre**
Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

**14. My genres**
Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

**15. Only Comedy**
Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.

**16. List shows and genres**
Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

================================================================================

