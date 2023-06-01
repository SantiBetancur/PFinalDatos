import pandas as pd

class ExcelDataframe():
    def __init__(self) -> None:
        self.df = pd.read_excel('aeropuertos.xlsx').drop_duplicates()
    
    def showDf(self):
        print(self.df)

    def searchCity(self,city):
        for i in range(len(self.df)):
            if city in self.df.iloc[i,2].replace("\xa0", ""):
                return self.df.iloc[i,0]
            
    def getAirports(self):
        l = []
        for i in range(len(self.df)):
            l.append(self.df.iloc[i,2].replace("\xa0",""))
    
        return l
    
    def getIATA(self):
        l = []
        for i in range(len(self.df)):
            l.append(self.df.iloc[i,0])
        return l    
 

    def searchAirportName(self, IATA):
        for i in range(len(self.df)):
            if IATA == self.df.iloc[i, 0]:
                return self.df.iloc[i, 1]  
             
    def searchAirportIATA(self, IATA):
        for i in range(len(self.df)):
            if IATA == self.df.iloc[i, 0]:
                return self.df.iloc[i, 0]           

    def searchIATA(self,IATA):
        for i in range(len(self.df)):
            if IATA == self.df.iloc[i,0]:
                return self.df.iloc[i,2]
            


