#!/usr/bin/python3
"""
-- Module --
Remove all states with the letter a
"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_state_a(username, password, db):
    """
    A function that deletes a state with the letter 'a'
    """
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{db}'
            )
    Session = sessionmaker(bind=engine)
    ss = Session()

    target_states = ss.query(State).filter(State.name.like('%a%')).all()

    for state in target_states:
        ss.delete(state)

    ss.commit()


if __name__ == '__main__':
    import sys

    if len(sys.argv) >= 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db = sys.argv[3]

        delete_state_a(username, password, db)
