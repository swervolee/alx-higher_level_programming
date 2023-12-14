#!/usr/bin/python3

import MySQLdb
import sys

myuser, password, database = sys.argv[1:]

db = MySQLdb.connect(host="localhost", user=myuser,
                     passwd=password, db=database)

cur = db.cursor()

cur.execute("SELECT cities.id, cities.name, states.name FROM cities left join states on cities.state_id = states.id order by cities.id")

rows = cur.fetchall()

for row in rows:
    print(row)
