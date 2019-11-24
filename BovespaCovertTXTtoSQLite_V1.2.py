from SQLite import *
from DayInformation import *

def CreateTables():
	sql = 'create table if not exists Stock (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, SHORT_NAME TEXT, CODE_OF_TRADING TEXT)'
	sQLite.ExecuteNonQuery(sql)
	sql = 'create table if not exists DailyStockInfo (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,IDStock INTEGER NOT NULL,Day TEXT NOT NULL,OpenPrice INTEGER NOT NULL,ClosePrice INTEGER NOT NULL,MaxPrice INTEGER NOT NULL,MinPrice INTEGER NOT NULL,AveragePrice INTEGER NOT NULL,BestPriceBuy INTEGER NOT NULL,BestPriceSale INTEGER NOT NULL,NumberOfBusiness INTEGER NOT NULL,TotalQuantityRoleMarket INTEGER NOT NULL,TotalVolumeRoleMarket TotalQuantityRoleMarket INTEGER NOT NULL)'
	sQLite.ExecuteNonQuery(sql)

def InsertDailyStockInfo(idStock, dailyStockInfo):
	sql =" SELECT ID FROM DailyStockInfo WHERE IDStock="+str(idStock)+" AND Day='"+dailyStockInfo.Date+"'"
	rows=sQLite.ExecuteQuery(sql)
	if rows != []:
		return rows[0][0]
	else:
		sql = "INSERT INTO DailyStockInfo (IDStock,Day,OpenPrice,ClosePrice,MaxPrice,MinPrice,AveragePrice,BestPriceBuy,BestPriceSale,NumberOfBusiness,TotalQuantityRoleMarket,TotalVolumeRoleMarket) VALUES ("+str(idStock)+",'"+dailyStockInfo.Date+"', "+str(dailyStockInfo.OpeningPeice)+", "+str(dailyStockInfo.LastPric)+", "+str(dailyStockInfo.MaximimPrice)+", "+str(dailyStockInfo.MinimumPrice)+", "+str(dailyStockInfo.AveragePrice)+", "+str(dailyStockInfo.BestPriceBuy)+", "+str(dailyStockInfo.BestPriceSale)+", "+str(dailyStockInfo.NumberOfBusiness)+", "+str(dailyStockInfo.TotalQuantityRoleMarket)+", "+str(dailyStockInfo.TotalVolumeRoleMarket)+")" 
		sQLite.ExecuteNonQuery(sql)


def InsertAllDailyStockInfoLite(idStock, allDailyStockInfo):
	query="INSERT INTO DailyStockInfo (IDStock,Day,OpenPrice,ClosePrice,MaxPrice,MinPrice,AveragePrice,BestPriceBuy,BestPriceSale,NumberOfBusiness,TotalQuantityRoleMarket,TotalVolumeRoleMarket) VALUES "
	for dailyStockInfo in allDailyStockInfo:
		query=query+"("+str(idStock)+",'"+dailyStockInfo.Date+"', "+str(dailyStockInfo.OpeningPeice)+", "+str(dailyStockInfo.LastPric)+", "+str(dailyStockInfo.MaximimPrice)+", "+str(dailyStockInfo.MinimumPrice)+", "+str(dailyStockInfo.AveragePrice)+", "+str(dailyStockInfo.BestPriceBuy)+", "+str(dailyStockInfo.BestPriceSale)+", "+str(dailyStockInfo.NumberOfBusiness)+", "+str(dailyStockInfo.TotalQuantityRoleMarket)+", "+str(dailyStockInfo.TotalVolumeRoleMarket)+")," 
	query=query[:-1]
	sQLite.ExecuteNonQuery(query)
		
#Inset in Database all Daily Stock Info
def InsertStock(allDailyStockInfo):
	if len(allDailyStockInfo) < 800:
		return
	id=GetStockID(allDailyStockInfo[0])
	#print (id)
	InsertAllDailyStockInfoLite(id,allDailyStockInfo)

def GetDailyStockInfoInDatabase(idStock):
	query =" SELECT Day FROM DailyStockInfo WHERE IDStock="+str(idStock)
	return sQLite.ExecuteQuery(query)


#Search the stock table for trading codes, if not find an insert in this table and return the ID
def GetStockID(dailyStockInfo):
	sql = "SELECT ID FROM Stock WHERE CODE_OF_TRADING = '"+dailyStockInfo.CodeOfTrading+"'" 
	rows=sQLite.ExecuteQuery(sql)	
	if rows != []:
		return rows[0][0]
	else:
		sql = "INSERT INTO Stock (SHORT_NAME, CODE_OF_TRADING) VALUES ('"+dailyStockInfo.ShortName+"','"+dailyStockInfo.CodeOfTrading+"')"
		sQLite.ExecuteNonQuery(sql)
		return GetStockID(dailyStockInfo)

def AddInDB(Alldata):
	CurrentCodeOfTrading=""
	AllDailyStockInfo=[]
	Alldata.sort(key=Get_CodeOfTrading)
	for DayInformationin in Alldata:
		if CurrentCodeOfTrading != DayInformationin.CodeOfTrading:
			print(CurrentCodeOfTrading)
			InsertStock(AllDailyStockInfo)
			AllDailyStockInfo.clear()
		AllDailyStockInfo.append(DayInformationin);

		CurrentCodeOfTrading=DayInformationin.CodeOfTrading
	#InsertStock(AllDailyStockInfo)

def LoadFileCallAddInDB(FileName):
	Alldata = []
	f = open(FileName)
	line = f.readline()
	while line:
		line = f.readline()
		DayInformationTemp=DayInformation(line)
		if(DayInformationTemp.RegisterType =="01"):
			Alldata.append(DayInformationTemp)
	f.close()
	print("Load completed")
	#AddInDB(Alldata)
	return Alldata

#Change here the name of database file!!!
CONST_NAME_DATABASE = 'ActionsInfo.db'

sQLite=SQLite(CONST_NAME_DATABASE)
sQLite.Open()
CreateTables()
Alldata = []
AllFileTXT=["COTAHIST_A2010.TXT","COTAHIST_A2011.TXT","COTAHIST_A2012.TXT","COTAHIST_A2013.TXT","COTAHIST_A2014.TXT","COTAHIST_A2015.TXT","COTAHIST_A2016.TXT","COTAHIST_A2017.TXT","COTAHIST_A2018.TXT"]
#AllFileTXT=["COTAHIST_A2010.TXT"]
for file in AllFileTXT:
	Alldata += LoadFileCallAddInDB("Files\\"+file)
	print(file)

AddInDB(Alldata)
sQLite.Close()
#input("Press Enter to continue...")