#!/usr/bin/python3
"""
A module to select cities by state
"""
import MySQLdb
import sys


def list_all_cities(usr, passwd, db):
    """
    A function to display all cities
    """
    db = MySQLdb.connect(host='localhost', port=3306, user=usr,
                         passwd=passwd, db=db)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name " +
                "FROM cities JOIN states ON states.id = " +
                "cities.state_id ORDER BY cities.id")
    for item in cur.fetchall():
        print(item)
    cur.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        usr = sys.argv[1]
        pswd = sys.argv[2]
        db = sys.argv[3]
        list_all_cities(usr, pswd, db)
