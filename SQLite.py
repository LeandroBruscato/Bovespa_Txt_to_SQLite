import sqlite3

CONST_NAME_DATABASE = 'ActionsInfo.db'
conn=None
cur=None

def Open():
	global conn
	conn = sqlite3.connect(CONST_NAME_DATABASE)
	global cur
	cur = conn.cursor()
	print("Open")
def Close():
	conn.commit()
	cur.close()
	conn.close()
	print("Close")
def ExecuteQuery(query):
	#conn = sqlite3.connect(CONST_NAME_DATABASE)
	#cur = conn.cursor()
	cur.execute(query)
	rows = cur.fetchall()
	#cur.close()
	conn.commit()
	return rows
	
def ExecuteNonQuery(query):
	cur.execute(query)
	conn.commit()

