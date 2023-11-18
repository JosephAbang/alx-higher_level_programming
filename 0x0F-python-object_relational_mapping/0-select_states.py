#!/usr/bin/python3
"""Script lists all states from the database"""

import sys
import MySQLdb

args = sys.argv

user_name = args[1]
passwrd = args[2]
database = args[3]
host = "localhost"
port = 3306

conn = MySQLdb.connect(host=host, user=user_name, passwd=passwrd, database=database, port=port)
curs = conn.cursor()
res = curs.execute("SELECT * FROM states ORDER BY state_id")
rows = curs.fetchall()
for row in rows:
    print(row)

curs.close()
conn.close()
