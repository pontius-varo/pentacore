#In this file, rooms will all be defined by the same class.
#collect room data (concept taken from Micheal Zalla's 'Room.py')
from . import index

class Room(object):

    name = None
    routes = []

    unvis = ""
    visted = ""

    visited = False

    def __init__(self, name, locked=False): #for now, use Mike's skeletion until I understand it further
    #check for a valid room
        validRm = False
        for key in index.rms:
            if key == name.upper():
                self.dataH = index.rms[key]
                validRm = True
        #valid room, collect room data
                self.name = name.upper()
                self.routes = self.dataH["ROUTES"]
                self.unvis = self.dataH["UNVISTED_TEXT"]
                self.vis = self.dataH["VISTED_TEXT"]

    def name(self): #returns the name of the room?
        return self.name

    def fetch_routes(self): #this method simply fetches the routes available to the player ie. "NORTH, SOUTH, EAST, DENNIS"
        out = ""
        for rou in self.routes:
            if self.routes[-1] != rou: #If less than one, a comma is displayed ?
                out += rou + ", "
            else:
                out += rou + ". " #if greater, a period is displayed
        return out

    def examine(self):
        ret = self.name + ': '
    #Gives the description of the room
        if (self.visited):
            ret += self.vis
        else:
            self.visited = True
            ret += self.unvis

    #show room connections
        ret += "Obvious exits are:"
        ret += self.fetch_routes()
        return ret

#def Look(self):
    #esp = ""
    #if(self.name !=)

    def HasItem(self, itemName):
        return self.inventory.HasItem(itemName)

    def addItems(self, items):
        self.inventory.addItems(items)

    def removeItems(self, itemNames):
        self.inventory.removeItems(Itemnames)
