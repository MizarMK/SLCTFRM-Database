import pymysql
import csv
import csi3335fall2021 as cfg
import sys
import warnings


def insert_data(file, table, ndx, cursor):
    file = open(file, "r")
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    statement = "INSERT INTO " + table + " VALUES ("
    for row in csvreader:
        vals = ""
        for i in ndx:
            if i is not None:
                vals += str("'" + row[i].replace("'", "''") + "'") + ", "
            else:
                vals += "'', "
        try:
            cursor.execute(statement + vals[0:-2] + ");")
        except Exception:
            print(statement + vals[0:-2] + ");")
            raise


def insert_div(table, dat, cursor):
    for d in dat:
        cursor.execute("INSERT INTO " + table + " VALUES (" + "'" + d + "', '" + dat[d] + "');")


lgIDs = {
    "AL": "American League",
    "AA": "American Association",
    "FL": "Federal League",
    "NA": "National Association",
    "NL": "National League",
    "PL": "Players League",
    "UA": "Union Association"}
divIDs = {
    "W": "West",
    "E": "East",
    "C": "Central"
}

con = pymysql.connect(host=cfg.mysql['host'], user=cfg.mysql['username'], password=cfg.mysql['password'])

try:
    cur = con.cursor()

    cur.execute("DROP DATABASE IF EXISTS `slctfrm`")
    print("Before:")
    sqlQuery = "SHOW DATABASES;"

    # Execute the sqlQuery
    cur.execute(sqlQuery)

    # Fetch all the rows
    databaseList = cur.fetchall()

    for database in databaseList:
        print(database)

    with open('slctfrm.sql') as f:
        returnList = f.read().split(";")
        for cmd in returnList:
            if cmd:
                cur.execute(cmd)

    print("After:")
    sqlQuery = "SHOW DATABASES;"
    cur.execute(sqlQuery)
    databaseList = cur.fetchall()

    for database in databaseList:
        print(database)

    sqlQuery = "SHOW TABLES;"
    cur.execute(sqlQuery)
    tableList = cur.fetchall()
    print("Tables:")
    for table in tableList:
        print(table)
    # People_ndx = [0, 13, 14, 15, 5, 4, 1, 2, 3, 18(n), 19(n), 1(c)]
    People_ndx = [0, 13, 14, 15, 5, 4, 1, 2, 3, 18, 19, 1]
    # Team_ndx = [None (autoID), 2, 0, 1, 3, None(playerID array Fix), None (GB), 10, 11, 12, 13, 8, 9, 6, 41 (ParkName fix]
    Team_ndx = [None, 2, 0, 1, 3, None, None, 10, 11, 12, 13, 8, 9, 6, 41]
    # Parks_ndx = [0, 1, 2, 3]
    Parks_ndx = [0, 1, 3, 4]

    insert_data("People.csv", "people", People_ndx, cur)
    insert_data("Teams.csv", "team", Team_ndx, cur)
    insert_data("Parks.csv", "parks", Parks_ndx, cur)
    insert_div("divisions", divIDs, cur)
    insert_div("leagues", lgIDs, cur)

# Exception handling
except Exception:
    con.rollback()
    print("Database exception")
    raise
else:
    con.commit()
finally:
    con.close()

# Pitcher/Batter
# yearID
# playerID
# teamID
#
# Appearances
# Appearances table