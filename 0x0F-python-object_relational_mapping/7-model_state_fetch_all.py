#!/usr/bin/python3
"""
Script lists all objects from database
"""

from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import (create_engine)
import sys

if __name__ == '__main__':
    args = sys.argv
    fmt_string = 'mysql+mysqldb://{}:{}@localhost/{}'
    fmt = fmt_string.format(args[1], args[2], args[3], pool_pre_ping=True)
    engine = create_engine(fmt)
    Base.metadata.create_all(engine)

    session = Session(engine)
    states = session.query(State).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()
