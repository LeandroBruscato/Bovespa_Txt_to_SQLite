from SQLite import *

def CreateTables():
	sql = 'create table if not exists Stock (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, SHORT_NAME TEXT, CODE_OF_TRADING TEXT)'
	ExecuteNonQuery(sql)
	sql = 'create table if not exists DailyStockInfo (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,IDStock INTEGER NOT NULL,Day TEXT NOT NULL,OpenPrice INTEGER NOT NULL,ClosePrice INTEGER NOT NULL,MaxPrice INTEGER NOT NULL,MinPrice INTEGER NOT NULL,AveragePrice INTEGER NOT NULL,BestPriceBuy INTEGER NOT NULL,BestPriceSale INTEGER NOT NULL,NumberOfBusiness INTEGER NOT NULL,TotalQuantityRoleMarket INTEGER NOT NULL,TotalVolumeRoleMarket TotalQuantityRoleMarket INTEGER NOT NULL)'
	ExecuteNonQuery(sql)

def InsertDailyStockInfo(idStock, dailyStockInfo):
	sql =" SELECT ID FROM DailyStockInfo WHERE IDStock="+str(idStock)+" AND Day='"+dailyStockInfo.Date+"'"
	rows=ExecuteQuery(sql)
	if rows != []:
		return rows[0][0]
	else:
		sql = "INSERT INTO DailyStockInfo (IDStock,Day,OpenPrice,ClosePrice,MaxPrice,MinPrice,AveragePrice,BestPriceBuy,BestPriceSale,NumberOfBusiness,TotalQuantityRoleMarket,TotalVolumeRoleMarket) VALUES ("+str(idStock)+",'"+dailyStockInfo.Date+"', "+str(dailyStockInfo.OpeningPeice)+", "+str(dailyStockInfo.LastPric)+", "+str(dailyStockInfo.MaximimPrice)+", "+str(dailyStockInfo.MinimumPrice)+", "+str(dailyStockInfo.AveragePrice)+", "+str(dailyStockInfo.BestPriceBuy)+", "+str(dailyStockInfo.BestPriceSale)+", "+str(dailyStockInfo.NumberOfBusiness)+", "+str(dailyStockInfo.TotalQuantityRoleMarket)+", "+str(dailyStockInfo.TotalVolumeRoleMarket)+")" 
		ExecuteNonQuery(sql)
		
#Inset in Database all Daily Stock Info
def InsertStock(allDailyStockInfo):
	if len(allDailyStockInfo) == 0:
		return
	id=GetStockID(allDailyStockInfo[0])
	for dailyStockInfo in allDailyStockInfo:
		InsertDailyStockInfo(id,dailyStockInfo)
	


def Get_PTOEXE(E):
	return E.PTOEXE
class DayInformation:
	def __init__(self, phrase):
		self.RegisterType = phrase[0:2]
		self.Date = phrase[2:10]
		self.CodeBDI= phrase[10:12]
		self.CodeOfTrading= phrase[12:24]
		self.MarketType	= phrase[24:27]
		self.ShortName = phrase[27:39]
		self.SpecificationOfPaper = phrase[39:49]
		self.DeadlineMarket	= phrase[49:52]
		self.ReferenceCurrency = phrase[52:56]
		self.OpeningPeice = phrase[56:69]
		self.MaximimPrice = phrase[69:82]
		self.MinimumPrice = phrase[82:95]
		self.AveragePrice	= phrase[95:108]
		self.LastPric = phrase[108:121]
		self.BestPriceBuy = phrase[121:134]
		self.BestPriceSale = phrase[134:147]
		self.NumberOfBusiness = phrase[147:152]
		self.TotalQuantityRoleMarket= phrase[152:170]
		self.TotalVolumeRoleMarket= phrase[170:188]
		self.PREEXE	= phrase[188:202]
		self.INDOPC	= phrase[202:202]
		self.DATVEN	= phrase[203:211]
		self.FATCOT	= phrase[211:218]
		self.FATCOT	= phrase[218:231]
		self.PTOEXE	= phrase[231:243]
		self.DISMES	= phrase[243:246]

def GetStockID(dailyStockInfo):
	sql = "SELECT ID FROM Stock WHERE CODE_OF_TRADING = '"+dailyStockInfo.CodeOfTrading+"'" 
	rows=ExecuteQuery(sql)	
	if rows != []:
		return rows[0][0]
	else:
		sql = "INSERT INTO Stock (SHORT_NAME, CODE_OF_TRADING) VALUES ('"+dailyStockInfo.ShortName+"','"+dailyStockInfo.CodeOfTrading+"')"
		return ExecuteGetIdQuery(sql)
	
def AddInDB(dailyStockInfo):
	id=GetStockID(dailyStockInfo)
	InsertDailyStockInfo(id,dailyStockInfo)

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
	Current_PTOEXE=""
	AllDailyStockInfo=[]
	Alldata.sort(key=Get_PTOEXE)
	for DayInformationin in Alldata:
		if Current_PTOEXE != DayInformationin.PTOEXE:
			InsertStock(AllDailyStockInfo)
			AllDailyStockInfo.clear()
		AllDailyStockInfo.append(DayInformationin);
		Current_PTOEXE=DayInformationin.PTOEXE
	InsertStock(AllDailyStockInfo)
Open()
CreateTables()
LoadFileCallAddInDB('COTAHIST_A2018.TXT')	
#LoadFileCallAddInDB('1.TXT')
Close()
input("Press Enter to continue...")
