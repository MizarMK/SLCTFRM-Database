import pymysql
from SLCTFRM import csi3335fall2021 as cfg

con = pymysql.connect(host=cfg.mysql['host'], user=cfg.mysql['username'], password=cfg.mysql['password'], database=cfg.mysql['database'])
cur = con.cursor()
cur.execute("SELECT DISTINCT teamName FROM teams")
results = cur.fetchall()
teams = ['None']
for row in results:
    for col in row:
        teams.insert(teams.__sizeof__(), col)
