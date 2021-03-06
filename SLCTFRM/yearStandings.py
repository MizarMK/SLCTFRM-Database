import pymysql
from SLCTFRM import csi3335fall2021 as cfg
from datetime import date
import sys
import warnings


# for testing
# con = pymysql.connect(host = 'localhost', user = 'root', password = 'pass', database = 'SLCTFRM')


def createStandings(year):
	paramYear = year
	str = ""
	con = pymysql.connect(host=cfg.mysql['host'], user=cfg.mysql['username'], password=cfg.mysql['password'], database=cfg.mysql['database'])
	cur = con.cursor()

	sql = "select distinct lgID from teams where yearID = %s"
	cur.execute(sql, (paramYear))
	leagueID = cur.fetchall()
	for row in leagueID:
		sql = "select distinct name from leagues where lgID = %s"
		cur.execute(sql, (row))
		league = cur.fetchone()
		#print()
		#print(league[0])
		#print()
		str += f",~{league[0]}~,,"
		sql = "select distinct divID, name from divisions where lgID = %s"
		cur.execute(sql, (row))
		division = cur.fetchall()
		lgID = row[0]
		if int(paramYear) < 1969:
			sql = "SELECT t.teamName, t.W, t.L, DivWin, WCWin, lgWin, WSWin FROM teams t, leagues l WHERE t.lgID = l.lgID AND t.yearID = %s AND t.lgID = %s GROUP BY t.teamID"
			cur.execute(sql, (paramYear, lgID))
			rows = cur.fetchall()
			LW = 0
			TW = 0
			LL = 150
			TL = 150
			DivWinner = ""
			WCWinner = ""
			lgWinner = ""
			WSWinner = ""
			for row in rows:
				if row[3] == "Y":
					DivWinner = row[0]
				if row[4] == "Y":
					WCWinner = row[0]
				if row[5] == "Y":
					lgWinner = row[0]
				if row[6] == "Y":
					WSWinner = row[0]
				if row[1] > LW:
					LW = row[1]
					if row[2] < LL:
						LL = row[2]
			for row in rows:
				TW = row[1]
				TL = row[2]
				GB = ((LW - TW) + (TL - LL)) / 2
				#print(row[0], " ", GB)
				str += f"{row[0]} -- {GB},"

			if DivWinner != "":
				#print("The division winner was", DivWinner)
				str += f"The division winner was {DivWinner},"
			if WCWinner != "":
				#print("The wild card winner was", WCWinner)
				str += f"The wild card winner was {WCWinner},"
			if lgWinner != "":
				#print("The league winner was", lgWinner)
				str += f"The league winner was {lgWinner},"
			if WSWinner != "":
				#print("The World Series winner was", WSWinner)
				str += f"The World Series winner was {WSWinner},"
		else:
			for each in division:
				sql = "SELECT t.teamName, t.W, t.L, DivWin, WCWin, lgWin, WSWin FROM teams t, divisions d WHERE t.lgID = d.lgID AND t.divID = d.divID AND t.yearID = %s AND t.lgID = %s AND d.divID = %s GROUP BY t.teamID"
				cur.execute(sql, (paramYear, lgID, each[0]))
				rows = cur.fetchall()
				# ommit empty divisons for NL and AL (central)
				if len(rows) > 1:
					#print(each[1])
					str += f"{each[1]}:,"
				LW = 0
				TW = 0
				LL = 150
				TL = 150
				DivWinner = ""
				WCWinner = ""
				lgWinner = ""
				WSWinner = ""
				for row in rows:
					if row[3] == "Y":
						DivWinner = row[0]
					if row[4] == "Y":
						WCWinner = row[0]
					if row[5] == "Y":
						lgWinner = row[0]
					if row[6] == "Y":
						WSWinner = row[0]
					if row[1] > LW:
						LW = row[1]
						if row[2] < LL:
							LL = row[2]
				for row in rows:
					TW = row[1]
					TL = row[2]
					GB = ((LW - TW) + (TL - LL)) / 2
					#print(row[0], " ", GB)
					str += f"{row[0]} -- {GB},"

				if DivWinner != "":
					#print("The division winner was", DivWinner)
					str += f"The division winner was {DivWinner},"
				if WCWinner != "":
					#print("The wild card winner was", WCWinner)
					str += f"The wild card winner was {WCWinner},"
				if lgWinner != "":
					#print("The league winner was", lgWinner)
					str += f"The league winner was {lgWinner},"
				if WSWinner != "":
					#print("The World Series winner was", WSWinner)
					str += f"The World Series winner was {WSWinner},"
				#print()
				str += ","
	#print()
	str += ","
	con.close()
	return str
