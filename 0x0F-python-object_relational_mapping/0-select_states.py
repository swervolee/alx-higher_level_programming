#!/usr/bin/python3
"""Connects to MySQLdb and selects all from the table states"""


import MySQLdb
import sys

if __name__ = "__main__":
    myuser, password, database = sys.argv[1:]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=myuser, passwd=password, db=database)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY ID")

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
