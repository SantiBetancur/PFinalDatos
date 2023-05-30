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
            sleep(2)
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
        origin = input("Enter origin airport IATA:\n")
        dest = input("Enter destination airpot IATA:\n")
        self.database.shortestRoute(origin,dest)


                