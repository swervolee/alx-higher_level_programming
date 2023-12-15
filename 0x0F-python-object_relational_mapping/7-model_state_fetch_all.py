#!/usr/bin/python3
"""Makes a query that selects all states"""


import sqlalchemy
from sqlalchemy import create_engine, text
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[
                               3], pool_pre_ping=True))

    conn = engine.connect()

    result = conn.execute(text("SELECT * FROM states"))

    rows = result.fetchall()

    for i in range(len(rows)):
        print(f"{i}: {rows[i][1]}")
