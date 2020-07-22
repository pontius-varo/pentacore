import sys

from libtes import core1 #replace 'libtes' to 'lib'
from libtes import index

from libtes import nav
from libtes import tools

from libtes import inv
from libtes import savstate

class Pentacore(object):

    verison = "0.03 'RELOADED'"

    #starting location
    currentRoom = "ROOM1"

    #Dictionary of Room Objects
    rooms = {}

    rm["ROOM1"] = core1.Room("ROOM1")
    rm["ROOM2"] = core1.Room("ROOM2")
    #additional rooms will be added later

    rmNames = []
    for rm in rooms.keys():
        rmNames.append(rm)


    #add items to a room

    rms["MOUNTAIN3"].addItems([Item.Item("RING")])
    rms["ROOM3"].addItems([Item.Item("SWORD")])

    def __init__(self):

    #Maybe attach a function to an item in order to forfill quest?

    Index.items["RING", "SWORD"]["PRESENT"] = self.presentItem

    self.inv = Inv.PlayerInventory([])

    self.intro()

    #waits for player to begin.
    while 1:
        cmd = input('>>>').upper() #might have to add .str before 'upper'
        if cmd.upper() == 'START':
            break
        elif cmd.lower() == 'QUIT':
            sys.exit()
        else:
            tools.Printer.output("I don't know what that means.")

    self.startx()

    def startx():
        self.examineRoom()
        while True:
            self.inteperateCmd(input(">>>")) #.rstrip*('\n ') ## I don't understand the purpose of this

    def interperateCmd(self, cmd):

        tools.printer.output("")
        cmd = cmd.upper()

        simpleCommands = {"EXIT": self.quit, "QUIT": self.quit,
                        "HELP": self.help, "EXAMINE ROOM": self.examineRoom,
                        "LOOK AROUND" : self.rms[self.currentrm].lookAround,
                        "INVENTORY" : self.showInv, "I": self.showInv,}

    #What's the point of checking whether or not it's a simple command

    for rmName in self.rmNames:
        if (cmd == "ENTER" + rmName) or (cmd == "GO TO" + rmName):
            #changing rooms is handled by self.changeRm()
            self.changeRoom(rmName)
            return
        #the following makes sure that the player examines only their current room
        if (cmd == "EXAMINE" + rmName):
            if rmName == self.currentrm:
                self.examineRm()
                return
        else:
            tools.Printer.output("You can't examine a room you aren't currently in.")

        for itemName in index.items:

            if cmd == "TAKE" + itemName or cmd == "PICK UP" + itemName:
                if self.rms[self.currentrm].HasItem(itemName):
                    self.rms[self.currentRm].removeItems([itemName])

                    item = Item.Item(itemName)
                    tools.Printer.output("Item:" + itemName + "has been added to your inventory.")
                    self.inv.addItems([item])
                    return
                else:
                    tools.Printer.output("I don't understand.")
                    return

            if cmd == ("EXAMINE" + itemName):
                #player is only able to examine items currently in the inventory
                if self.inv.hasItem(itemName) or self.rms[self.currentRm].hasItem(itemName):
                    tools.Printer.output(tools.items[itemName]["DESC"])
                    return

            if cmd == ("USE" + itemName): #might have to refine this
                if self.inv.hasItem(itemName):
                tools.Printer.output("Sorry, you can't actually use this item!")
            else:
                return

            #here be a check to see if the user wants to add "WITH" to a "USE" statement

            #$$$CHANGEROOM$$$#
            def changeRm(self, rmName):
                if roomName == self.currentRm:
                    tools.Printer.output("You're already in that area, dumbass")
                    return

                #validMoves = self.rms[self.currentRm].routes
                #for move in validMoves:
                    #if rmName == move:
                        #if (self.rms[rmName].locked == False):
                        #self.currentRoom = rmName
                        #self.examineRoom()
                        #return
                    #else:
                        #tools.Printer.output(Data.rms[rmName]["LOCKED_MSG"])
                #tools.Printer.output("That isn't a nearby room.")
                #return

            def examineRm(self):
                tools.Printer.output("")
                tools.Printer.output("0++++++++++++++++++++++0")
                tools.Printer.output(self.rms[self.currentRm].examine())

            def intro(self): #might want to use a different printer for this!
                tools.Printer.output("")
                tools.Printer.output("0++++++++++++++++++++++0")

                tools.Printer.output("""Welcome to Pentacore, ver. %s! The premier text-adventure game since 2020.
                """ % version, "Developed by Pontius Varo. ©Eltersoft. All rights reserved.")

                tools.Printer.output("This game operates similarily to ZORK. Figure out the commands yourself or type HELP.")
                tools.Printer.output("To begin, type start and press enter.")
                tools.Printer.output("To exit, type quit and press enter.")

            def help(self):
                tools.Printer.output("0++++++++++++++++++++++0")
                tools.Printer.output("Git Gud Menu:")
                tools.Printer.output("The following are valid commands:")
                tools.Printer.output("'EXAMINE X', 'PRESENT X', 'LOOK', 'USE X', 'I', 'INVENTORY',")
                tools.Printer.output("'GO TO X', 'SPEAK TO X', 'TALK TO X', 'SUDOKU'")
                tools.Printer.output("That's it, figure everything out yourself numbskull. Now GIT GUD.")
                tools.Printer.output("0++++++++++++++++++++++0")

            def quit(self):
                sys.exit()

            def showInv():
                self.inv.display()

            def death_via_grue():
                if self.currentRoom == "ROOM3": #add more rooms. btw I don't think this is working properly.
                    tools.Printer.output("Suddenly, a GRUE arises from the darkness and consumes you.")
                    tools.Printer.output("Congratulations, you are now dead.")
