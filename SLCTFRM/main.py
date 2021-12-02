import os.path

import pymysql
import csv
import csi3335fall2021 as cfg

# League and Division IDs dictionaries
lgIDs = {
    "AL": "American League",
    "AA": "American Association",
    "FL": "Federal League",
    "NA": "National Association",
    "NL": "National League",
    "PL": "Players League",
    "UA": "Union Association"}
here = os.path.dirname(os.path.abspath(__file__))

# Function to insert data into a table.
#   file: name of the csv file
#   table: name of the table to insert into
#   ndx: array of integers that refer to the index of header to grab data from
#   cursor: the sql cursor object
def insert_data(file, table, ndx, cursor):
    file = os.path.join(here,file)

    file = open(file, "r")
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        statement = "INSERT INTO " + table + " VALUES ("
        vals = ""
        for i in ndx:
            if i is not None:
                vals += str("'" + row[i].replace("'", "''") + "'") + ", "
            else:
                vals += "'', "
        try:
            statement = statement + vals[0:-2] + ");"
            statement = statement.replace("'', ", "NULL, ")
            statement = statement.replace(", ''", ", NULL")
            cursor.execute(statement)
        except Exception:
            print(statement + vals[0:-2] + ");")
            raise


# Small function to insert the division and league IDs
def insert_div(table, dat, cursor):
    for d in dat:
        cursor.execute("INSERT INTO " + table + " VALUES (" + "'" + d + "', '" + dat[d] + "');")


con = pymysql.connect(host=cfg.mysql['host'], user=cfg.mysql['username'], password=cfg.mysql['password'])

try:
    cur = con.cursor()
    file = os.path.join(here, 'slctfrm.sql')

    with open(file) as f:
        returnList = f.read().split(";")
        for cmd in returnList:
            if cmd.strip() != "":
                cur.execute(cmd)


    # Insert the data into the tables here
    # People_ndx = [0, 13, 14, 15, 5, 4, 1, 2, 3, 18(n), 19(n), 1(c)]
    People_ndx = [0, 13, 14, 15, 5, 4, 1, 2, 3]
    # Teams_ndx = [None (autoID), 2, 0, 1, 3, None(playerID array Fix), None (GB), 10, 11, 12, 13, 8, 9, 6, 41 (ParkName fix]
    Teams_ndx = [None, 2, 0, 1, 3, 10, 11, 12, 13, 8, 9, 6, 41, 40]

    # Parks_ndx = [0, 1, 2, 3]
    Parks_ndx = [0, 1, 3, 4]
    # Batting_ndx = [None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    Batting_ndx = [None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # Pitching_ndx = [None, 0, 1, 2, 3, 4, 5, 6, 7]
    Pitching_ndx = [None, 0, 1, 2, 3, 4, 5, 6, 7]
    # Appearances_ndx = [None, 0, 1, 2, 3, 4, 6, 8]
    Appearances_ndx = [None, 0, 1, 2, 3, 4, 6, 8]

    insert_data("People.csv", "people", People_ndx, cur)
    print("People Done.")

    insert_data("Teams.csv", "teams", Teams_ndx, cur)
    print("Teams Done.")

    insert_data("Parks.csv", "parks", Parks_ndx, cur)
    print("Parks Done.")

    insert_data("Batting.csv", "batting", Batting_ndx, cur)
    print("Batting Done.")

    insert_data("Pitching.csv", "pitching", Pitching_ndx, cur)
    print("Pitching Done.")

    insert_data("Appearances.csv", "appearances", Appearances_ndx, cur)
    print("Apps Done.")

    insert_div("leagues", lgIDs, cur)
    print("Leagues Done.")


# Exception handling
except Exception:
    con.rollback()
    print("Database exception")
    raise
else:
    con.commit()
finally:
    con.close()
