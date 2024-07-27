#!/usr/bin/python3
"""
Select all the states in a database
"""
import sys
import MySQLdb


def select_states(user, passwd, db_name):
    """
    A function to select all the states in a database
    """

    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         passwd=passwd, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    """
    query the passed in argz
    """
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    select_states(user, passwd, db_name)
