#!/usr/bin/python3
"""Makes a query that selects all cities from a given state"""


import MySQLdb
import sys

if __name__ == '__main__':
    myuser, password, database, state_name = sys.argv[1:]

    db = MySQLdb.connect(
        host="localhost",
        user=myuser,
        passwd=password,
        db=database,
        port=3306
    )

    cur = db.cursor()

    cur.execute("""
    SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name=%s""", (state_name,))

    rows = cur.fetchall()

    for row in rows:
        if row != rows[-1]:
            print(f"{row[0]}, ", end="")
        else:
            print(f"{row[0]}")
