#!/usr/bin/python3
"""makes a query using given search"""

import MySQLdb
import sys

if __name__ == "__main__":
    myuser, password, database, search = sys.argv[1:]

    db = MySQLdb.connect(host="localhost", user=myuser, port=3306,
                         passwd=password, db=database)

    cur = db.cursor()

    cur.execute(f"SELECT * FROM states WHERE name='{search}' ORDER BY id")

    rows = cur.fetchall()

    for row in rows:
        print(row)
