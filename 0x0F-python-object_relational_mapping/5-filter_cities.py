#!/usr/bin/python3
"""
A module to select cities by state
"""
import MySQLdb
import sys


def cities_of_a_state(usr, passwd, db, state):
    """
    A function to display all cities
    """
    cities = []
    db = MySQLdb.connect(host='localhost', port=3306, user=usr,
                         passwd=passwd, db=db)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON " +
                f"cities.state_id = states.id WHERE states.name = '{state}'")
    for item in cur.fetchall():
        cities.append(item[0])
    cities = ", ".join(cities)
    print(cities)
    cur.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        usr = sys.argv[1]
        pswd = sys.argv[2]
        db = sys.argv[3]
        state = sys.argv[4]
        cities_of_a_state(usr, pswd, db, state)
