#!/usr/bin/python3
"""Script lists all matched states"""

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
    q = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(_match)
    curs.execute(q)
    rows = curs.fetchall()
    for row in rows:
        print(row)

    curs.close()
    conn.close()
