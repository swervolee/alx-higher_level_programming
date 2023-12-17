#!/usr/bin/python3
"""makes a joined query between city and state"""


import sqlalchemy
from sqlalchemy import create_engine, text
from model_state import Base, State
from model_city import City
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[
                               3], pool_pre_ping=True))

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(engine)

    session = Session()

    for st, ct in session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id):
        print(f'{st.name}: ({ct.id}) {ct.name}')
