#!/usr/bin/python3
"""Creates a new state and inserts it into the database"""


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

    search = session.query(State).filter_by(id=2).one()

    search.name = 'New Mexico'

    session.commit()
