#!/usr/bin/python3
"""Lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    mycur = mydb.cursor()

    mycur.execute("SELECT * FROM states WHERE name LIKE 'N%';")
    states = mycur.fetchall()

    for state in states:
        print(state)    
    