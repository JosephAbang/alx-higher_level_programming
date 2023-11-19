#!/usr/bin/python3
"""Script lists all cities of a given state"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv

    usr = args[1]
    pwd = args[2]
    db = args[3]
    ht = "localhost"
    pt = 3306
    _match = args[4]

    conn = MySQLdb.connect(host=ht, user=usr, passwd=pwd, database=db, port=pt)
    curs = conn.cursor()
    query = """SELECT name
                FROM cities
                WHERE state_id = (
                    SELECT id
                    FROM states
                    WHERE name = '{}'
                )
                ORDER BY id
            """.format(_match)
    res = curs.execute(query)
    rows = curs.fetchall()
    city_names = ', '.join(row[0] for row in rows)
    print(city_names)
    curs.close()
    conn.close()
