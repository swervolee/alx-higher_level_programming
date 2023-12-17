#!/usr/bin/python3
"""Selects all states that have the letter 'a'"""


import sqlalchemy
from sqlalchemy import create_engine, text
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[
                               3], pool_pre_ping=True))

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(engine)

    session = Session()

    for item in session.query(State).filter(State.name.
                                            like("%a%")).order_by(State.id):
        session.delete(item)

    session.commit()
