import pandas as pd

class ExcelDataframe():
    def __init__(self) -> None:
        self.df = pd.read_excel('aeropuertos.xlsx')
    
    def showDf(self):
        print(self.df)

    def searchCity(self,city):
        for i in range(len(self.df)):
            if city in self.df.iloc[i,2]:
                return self.df.iloc[i,0]
            
    def getAirports(self):
        l = []
        for i in range(len(self.df)):
            l.append(self.df.iloc[i,2])
        l1 = [item.replace('\xa0',' ') for item in l]
        return l1
        
    def searchIATA(self,IATA):
        for i in range(len(self.df)):
            if IATA == self.df.iloc[i,0]:
                return self.df.iloc[i,2]
            

