#!/usr/bin/python3
'''
A module
'''
import sys
import MySQLdb


def list_states(username, password, name, state_name):
    '''
    an function that prints a db
    '''
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=name)

    cursor = db.cursor()
    query = '''SELECT * FROM states
            WHERE BINARY name = '{}' ORDER BY id ASC'''.format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state = sys.argv[4]

    list_states(username, password, db, state)
