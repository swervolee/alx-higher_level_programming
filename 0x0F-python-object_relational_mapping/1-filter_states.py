#!/usr/bin/python3
"""Makes a query that selects all states starting with 'N'"""


import MySQLdb
import sys

if __name__ == "__main__":
    myuser, password, database = sys.argv[1:]

    db = MySQLdb.connect(host="localhost", user=myuser, port=3306,
                         passwd=password, db=database)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")

    rows = cur.fetchall()

    for row in rows:
        print(row)
