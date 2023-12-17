#!/usr/bin/python3
"""Makes a query that selects the first state"""


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

    result = session.query(State).filter_by(id=1).first()

    print(result.id, result.name, sep=": ")
