#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the database
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sys import argv
from sqlalchemy.orm import Session

if __name__ == '__main__':
    fmt_string = 'mysql+mysqldb://{}:{}@localhost/{}'
    fmt = fmt_string.format(argv[1], argv[2], argv[3], pool_pre_ping=True)
    engine = create_engine(fmt)
    Base.metadata.create_all(engine)

    session = Session(engine)
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        print(f'{state.id}: {state.name}')
    session.close()
