#!/usr/bin/python3
''' file-name: 4-cities_by_state.py '''


import MySQLdb
from sys import argv

# this code will not work if it was imported.
if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # clean up process.
    cursor.close()
    connection.close()
