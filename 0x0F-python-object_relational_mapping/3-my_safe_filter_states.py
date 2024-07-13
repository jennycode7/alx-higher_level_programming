#!/usr/bin/python3
import sys
import MySQLdb


def find_state(username, password, db_name, state_name):
    # Connect to the MySQaL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows in a list of tuples
    rows = cursor.fetchall()

    # Loop through the rows and print them
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to find and display the state
    find_state(username, password, db_name, state_name)
