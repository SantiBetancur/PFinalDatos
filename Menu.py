from AeropuertosBack import Graph
from time import sleep

class Menu():
    def __init__(self) -> None:
        self.database = Graph()

    def mainMenu(self):
        def showMenu():
            uopt = input(f'Please, select an option!\n1)Show all airports\n2)Show most economic route between airports\n3)Add new route\n0)Exit\n')
            return int(uopt)

        print("********Welcome to AirportDB!********")
        while True:
            sleep(1)
            opt = showMenu()
            if opt == 1:
                self.database.showGraph()
            elif opt == 2:
                self.mostEconomic()
            elif opt == 3:
                self.addNewRoute()
            elif opt == 0:
                print("Exiting...\n")
                break
            else:
                print("Invalid option, please try again\n")

    def addNewRoute(self):
        origin = input("Enter origin airport IATA:\n")
        dest = input("Enter destination airpot IATA:\n")
        price = int(input("Enter price of new route:\n"))
        self.database.addNewRoute(origin,dest,price)

    def mostEconomic(self):

        dests = []
        def findNeighbors(ori):
            l = list(self.database.Graph.neighbors(ori))
            for i in l:
                dests.append(i)
                findNeighbors(i)
            
        origins = set(self.database.dfc['origen'])
        print(f'The available origin airports are: \n{origins}\n')
        origin = input("Enter origin airport IATA:\n")
        if origin not in origins:
            print("Invalid origin city\n")
            return
        findNeighbors(origin)
        print(f'The available destinations from this airport are: \n{dests}\n')
        dest = input("Enter destination airpot IATA:\n")
        self.database.shortestRoute(origin,dest)


                