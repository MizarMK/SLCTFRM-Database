import pymysql

user = 'root'
passw = 'pass'
host = 'localhost'
db = 'SLCTFRM'

con = pymysql.connect(host=host, user=user, password=passw, database=db)
cur = con.cursor()
cur.execute("SELECT DISTINCT teamid FROM teams")
results = cur.fetchall()
teams = ['None']
for row in results:
    for col in row:
        teams.insert(teams.__sizeof__(), col)
