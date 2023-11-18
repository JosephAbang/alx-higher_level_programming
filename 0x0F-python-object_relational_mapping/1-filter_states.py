#!/usr/bin/python3
"""script returns filtered list"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv

    usr = args[1]
    pwd = args[2]
    db = args[3]
    ht = "localhost"
    pt = 3306

    con = MySQLdb.connect(host=ht, user=usr, passwd=pwd, database=db, port=pt)
    curs = con.cursor()
    result = curs.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    rows = curs.fetchall()
    for row in rows:
        print(row)
