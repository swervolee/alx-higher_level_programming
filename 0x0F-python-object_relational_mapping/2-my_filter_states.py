#!/usr/bin/python3
"""makes a query using given search"""

import MySQLdb
import sys

if __name__ == "__main__":
    myuser, password, database, search = sys.argv[1:]

    db = MySQLdb.connect(host="localhost", user=myuser, port=3306,
                         passwd=password, db=database)

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name=%s ORDER BY id"

    cur.execute(query, (search,))

    rows = cur.fetchall()

    for row in rows:
        print(row)
