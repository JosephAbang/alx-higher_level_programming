#!/usr/bin/python3
"""Script lists all matched states and prevents SQL injection"""

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

    conn = MySQLdb.connect(host=ht, user=usr, passwd=pwd, db=db, port=pt)
    curs = conn.cursor()
    q = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    curs.execute(q, (_match,))
    rows = curs.fetchall()
    for row in rows:
        print(row)

    curs.close()
    conn.close()
