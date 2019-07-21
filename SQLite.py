import sqlite3
#from System import Data
#from System.Data import DataTable

class SQLite:
	def __init__(self, databaseName):
		self.database_name = databaseName
		self.conn=None
		self.cur=None

	def Open(self):
		self.conn = sqlite3.connect(self.database_name)
		self.cur = self.conn.cursor()
		print("Open")
	def Close(self):
		self.conn.commit()
		self.cur.close()
		self.conn.close()
		print("Close")
	def ExecuteQuery(self,query):
		#conn = sqlite3.connect(CONST_NAME_DATABASE)
		#cur = conn.cursor()
		self.cur.execute(query)
		rows = self.cur.fetchall()
		#cur.close()
		self.conn.commit()
		return rows
		
	def ExecuteNonQuery(self,query):
		self.cur.execute(query)
		self.conn.commit()
	

