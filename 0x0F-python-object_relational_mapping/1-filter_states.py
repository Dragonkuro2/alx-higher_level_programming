#!/usr/bin/python3
''' file-name: 1-filter_states.py '''


import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%'"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
