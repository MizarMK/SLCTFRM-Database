import pymysql
import csi3335fall2021 as cfg
import sys
import warnings
from datetime import date


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    return age


# Checks for the correct amount of arguments
params = []
argc = len(sys.argv)
if argc != 2:
    sys.stderr.write("Error in argument count!")
    exit(1)
else:
    params = sys.argv[1]

# Connects to the database
con = pymysql.connect(host=cfg.mysql['host'], user=cfg.mysql['username'], password=cfg.mysql['password'],
                      database=cfg.mysql['database'])
warnings.simplefilter("ignore")

# Sets up the SQL query to send to database
try:
    year = 2020
    playerName = ""
    playerAge = 0
    birthPlace = None
    hitter = True
    pitcher = False

    cur = con.cursor()
    sql = '''SELECT p.playerID, ppl.nameFull as 'Name', ppl.birthCountry, ppl.birthYear,
     ppl.birthMonth, ppl.birthDay
     FROM pitching p JOIN batting b ON (b.yearID = p.yearID AND b.playerID = p.playerID)
     JOIN people ppl ON (ppl.personID = p.playerID)
     WHERE p.yearID = 2020 AND p.teamID = %s'''
    cur.execute(sql, params)

    # Gets the results from the query and prints them out
    finalResults = []
    results = cur.fetchall()
    for row in results:
        finalResults.append([row[0], row[1], row[2], calculateAge(date(row[3], row[4], row[5])), "N", "N"])

    # [playerID, name, birth, age, pitcher, batter]
    for row in finalResults:
        params = row[0]
        sql = '''SELECT playerID FROM appearances WHERE G_batting > 0 AND playerID = %s'''
        cur.execute(sql, params)
        results = cur.fetchall()
        if len(results) > 0:
            row[5] = "Y"
        sql = '''SELECT playerID FROM appearances WHERE G_pitcher > 0 AND playerID = %s'''
        cur.execute(sql, params)
        results = cur.fetchall()
        if len(results) > 0:
            row[4] = "Y"

    for r in finalResults:
        r.pop(0)
        for c in r:
            print(c, end=", ")
        print()

# Exception handling
except Exception:
    con.rollback()
    print("Database exception")
    raise
else:
    con.commit()
finally:
    con.close()
