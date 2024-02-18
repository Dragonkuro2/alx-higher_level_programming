#!/usr/bin/python3
''' file-name: 2-my_filter_states.py '''

import MySQLdb
from sys import argv

# this program will not work if the file was imported.
if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cursor.execute(query, (argv[4], ))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # clean up the memory after our process is done.
    cursor.close()
    connection.close()
