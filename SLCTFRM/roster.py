import pymysql
import csi3335fall2021 as cfg
import warnings
from datetime import date


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    return age


# Connects to the database
con = pymysql.connect(host=cfg.mysql['host'], user=cfg.mysql['username'], password=cfg.mysql['password'],
                      database=cfg.mysql['database'])
warnings.simplefilter("ignore")

# HERE IS WHERE YOU PUT THE TEAMID AND YEARID FOR THE ROSTER YOU WANT
params = ["HOU", "2020"]

# Sets up the SQL query to send to database
try:
    cur = con.cursor()
    sql = '''SELECT p.playerID, concat(ppl.nameFirst, ' ', ppl.nameLast) as 'Name', ppl.birthCountry, ppl.birthYear,
     ppl.birthMonth, ppl.birthDay
     FROM appearances p JOIN people ppl ON (ppl.personID = p.playerID)
     WHERE p.teamID = %s AND p.yearID = %s'''
    cur.execute(sql, params)

    # Gets the results from the query and prints them out
    finalResults = dict()
    results = cur.fetchall()
    for row in results:
        finalResults[row[0]] = ([row[1], row[2], calculateAge(date(row[3], row[4], row[5])), "N", "N"])

    # Key: playerID, Value: [name, birth, age, pitcher, batter]
    # This sorts it into last name order
    for row in dict(sorted(finalResults.items(), key=lambda item: item[1])):
        params[0] = row
        sql = '''SELECT playerID FROM appearances WHERE G_batting > 0 AND playerID = %s AND yearID = %s'''
        cur.execute(sql, params)
        results = cur.fetchall()
        if len(results) > 0:
            temp = finalResults[row]
            temp[4] = "Y"
            finalResults[row] = temp
        sql = '''SELECT playerID FROM appearances WHERE G_pitcher > 0 AND playerID = %s AND yearID = %s'''
        cur.execute(sql, params)
        results = cur.fetchall()
        if len(results) > 0:
            temp = finalResults[row]
            temp[3] = "Y"
            finalResults[row] = temp

    for r in finalResults:
        for c in finalResults[r]:
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
