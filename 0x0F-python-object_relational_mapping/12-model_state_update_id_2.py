#!/usr/bin/python3
"""
Updates object using id
"""

from sqlalchemy.orm import Session
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State

if __name__ == '__main__':
    fmt_string = 'mysql+mysqldb://{}:{}@localhost/{}'
    fmt = fmt_string.format(argv[1], argv[2], argv[3], pool_pre_ping=True)
    engine = create_engine(fmt)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state_update = session.query(State).filter_by(id=2).first()
    state_update.name = 'New Mexico'
    session.commit()
    session.close()
