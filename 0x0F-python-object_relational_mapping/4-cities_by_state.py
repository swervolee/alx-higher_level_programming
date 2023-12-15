#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    myuser, password, database = sys.argv[1:]

    db = MySQLdb.connect(
        host="localhost",
        user=myuser,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        ORDER BY cities.id
    """)

    rows = cur.fetchall()

    for row in rows:
        print(row)
