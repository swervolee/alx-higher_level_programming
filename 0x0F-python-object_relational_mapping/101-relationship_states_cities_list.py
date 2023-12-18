#!/usr/bin/python3
"""PRINTING STATES AND CITIES USING RELATIONSHIP"""


import sqlalchemy
from sqlalchemy import create_engine, text
from relationship_state import Base, State
import sys
from relationship_city import City
from sqlalchemy.orm import sessionmaker, joinedload

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[
                               3], pool_pre_ping=True))

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(engine)

    session = Session()

    for st in session.query(State).filter(
            State.id == City.state_id).order_by(State.id, City.id):
        print(st.id, st.name, sep=': ')

        for ct in st.cities:
            print('    ' + str(ct.id), ct.name, sep=': ')
