#!/usr/bin/python3
''' file-name: 0-select_states.py '''


import MySQLdb
from sys import argv

# with this condion the code will should not work when imported.
if __name__ == "__main__":
    # making connection to the database
    connection = MySQLdb.connect(host = "localhost", port = 3306,
            user = argv[1], passwd = argv[2], db = argv[3])
    cursor = connection.cursor()
    query = "SELECT * FROM states"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    #we use the methode close() to clean up the process after they done.
    cursor.close()
    connection.close()
