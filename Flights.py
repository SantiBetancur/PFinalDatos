import random

class Flight():

  def __init__(self, origin, destiny):
    self.airline = random.choice(["LATAM", "AVIANCA", "DELTA", "QATAR", "VIVA", "EMIRATES"])
    
    #For stablish a random flight number, i´m used an array of prefix
    prefix = ["AA", "AK" , "AB" , "AL", "BB","BL" , "BK" , "BT" ,"CC", "CK" , "CL" , "CF" ,"EE", "EF", "EK" ]
    self.flight_number = random.choice(prefix)+str(random.randint(100, 999)) 
    
    self.type = "WAITING"


    self.airport_origin =  origin
    self.airport_destiny = destiny
   
    self.time = {"HOUR" : random.randint(0, 23), "MINUTES": random.randint(0, 59)}

    if self.time["HOUR"] < 10:
      self.date_start = (f'0{self.time["HOUR"]}:{self.time["MINUTES"]}')
    elif self.time["MINUTES"] < 10:
      self.date_start = (f'{self.time["HOUR"]}:0{self.time["MINUTES"]}')
    elif self.time["HOUR"] < 10 and self.time["MINUTES"] < 10:
      self.date_start = (f'0{self.time["HOUR"]}:0{self.time["MINUTES"]}')
    else:
      self.date_start = (f'{self.time["HOUR"]}:{self.time["MINUTES"]}')
      
    self.duration = random.randint(60, 180)
  
    #The priority is defined with a probabilty, stablish COMMERCIAL with the mayority (60%)
    priorities_opt = [{"N":"EMERGENCY", "VALUE": 1}, {"N":"MILITARY", "VALUE": 2} , {"N":"COMMERCIAL", "VALUE": 3}]
    wg = [15, 15 , 60]
    pr_list = random.choices(priorities_opt, weights= wg, k = 1)
    self.priority = pr_list[0]  