#Used to group data from the same trading codes
def Get_PTOEXE(E):
	return E.PTOEXE
def Get_CodeOfTrading(E):
	return E.CodeOfTrading
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