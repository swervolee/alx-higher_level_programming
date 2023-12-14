#!/usr/bin/python3
"""Connects to MySQLdb and selects all from the table states"""


import MySQLdb
import sys

myuser, password, database = sys.argv[1:]

db = MySQLdb.connect(host="localhost",
                     user=myuser, passwd=password, db=database)

cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY ID")

rows = cur.fetchall()

for row in rows:
    print(row)
