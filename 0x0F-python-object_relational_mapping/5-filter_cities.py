#!/usr/bin/python3
''' file-name: 5-filter_cities.py '''


import MySQLdb
from sys import argv

# this code will not work if it was imported.
if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    query = "SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s"
    cursor.execute(query, (argv[4], ))
    rows = cursor.fetchall()
    tmp = []
    for row in rows:
        tmp.append(row[0])
    print(", ".join(tmp))

    # clean up process.
    cursor.close()
    connection.close()
