#!/usr/bin/python3
'''
A module
'''
import sys
import MySQLdb


def states_with_N(username, password, name):
    '''
    an function that prints a db
    '''
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=name)

    cursor = db.cursor()
    cursor.execute('''SELECT * FROM states
                   WHERE name LIKE BINARY 'N%' ORDER BY id ASC''')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    states_with_N(username, password, db)
