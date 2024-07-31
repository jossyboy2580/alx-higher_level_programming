#!/usr/bin/python3
"""
This module contains a function that updates an
item from the database
"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def update_state(username, password, db):
    """
    This function updates the name of the state
    with id 2 to 'New Mexico'
    """
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{db}'
            )
    Session = sessionmaker(bind=engine)
    ss = Session()

    target_state = ss.query(State).filter(State.id == 2).first()
    target_state.name = 'New Mexico'
    ss.commit()


if __name__ == '__main__':
    import sys

    if len(sys.argv) >= 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db = sys.argv[3]

        update_state(username, password, db)
