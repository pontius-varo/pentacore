import sys

from lib import Abraham, Index, Inv
from lib import Tools

class Pentacore(object):

    version = "0.03 'RELOADED'"

    #starting location
    currentRoom = "ROOM1"

    #Dictionary of Room Objects
    rms = {}

    rms["ROOM1"] = Abraham.Room("ROOM1", True)
    rms["ROOM2"] = Abraham.Room("ROOM2", True)
    #additional rooms will be added later

    rmNames = []
    for rm in rms.keys():
        rmNames.append(rm)


    #add items to a room

    #rms["MOUNTAIN3"].addItems([Item.Item("RING")])
    #rms["ROOM3"].addItems([Item.Item("SWORD")])

    def __init__(self):
        Index.items["SWORD"]["PRESENT"] = self.presentItem1
        Index.items["RING"]["PRESENT"] = self.presentItem2

        self.inv = Inv.PlayerInventory([])

        self.intro()

    #waits for player to begin.
        while 1:
            cmd = input('>>>').upper() #might have to add .str before 'upper'
            if cmd.upper() == 'START':
                break
            if cmd.upper() == 'QUIT':
                sys.exit()
            else:
                Tools.Printer.output("I don't know what that means.")

        self.startx()

    def startx(self):
        self.examineRm()
        while True:
            self.interperateCmd(input(">>> ")) #.rstrip*('\n ') ## I don't understand the purpose of this

    def interperateCmd(self, cmd):

        Tools.Printer.output("")
        cmd = cmd.upper()

        simpleCommands = { "EXIT": self.quit, "QUIT": self.quit,
                            "HELP": self.help, "EXAMINE ROOM": self.examineRm,
                        #"LOOK AROUND" : self.rms[self.currentRoom].lookAround,
                            "INVENTORY" : self.showInv, "I": self.showInv,
                            "SUDOKU":self.sudoku }

    #What's the point of checking whether or not it's a simple command
        for c in simpleCommands:
            if cmd == c:
                simpleCommands[c]()
                return

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
                    Tools.Printer.output("You can't examine a room you aren't currently in.")

        for itemName in Index.items:

            if cmd == "TAKE" + itemName or cmd == "PICK UP" + itemName:
                if self.rms[self.currentrm].HasItem(itemName):
                    self.rms[self.currentRm].removeItems([itemName])

                    item = Item.Item(itemName)
                    Tools.Printer.output("Item:" + itemName + "has been added to your inventory.")
                    self.inv.addItems([item])
                    return
                else:
                    Tools.Printer.output("I don't understand.")
                    return

            if cmd == ("EXAMINE" + itemName):
                #player is only able to examine items currently in the inventory
                if self.inv.hasItem(itemName) or self.rms[self.currentRm].hasItem(itemName):
                    Tools.Printer.output(tools.items[itemName]["DESC"])
                    return

            if cmd == ("USE" + itemName): #might have to refine this
                if self.inv.hasItem(itemName):
                    Tools.Printer.output("Sorry, you can't actually use this item!")
            else:
                return

            #here be a check to see if the user wants to add "WITH" to a "USE" statement

            #$$$CHANGEROOM$$$#
    def changeRm(self, rmName):
        if roomName == self.currentRm:
            Tools.Printer.output("You're already in that area, dumbass")
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
        Tools.Printer.output("")
        Tools.Printer.output("0++++++++++++++++++++++0")
        Tools.Printer.output(self.rms[self.currentRoom].examine())

    def intro(self): #might want to use a different printer for this!
        Tools.Printer.output("")
        Tools.Printer.output("0++++++++++++++++++++++0")
        Tools.Printer.output("")
        Tools.Printer.output("Welcome to Pentacore! The premier text-adventure game since 2020.")
        Tools.Printer.output("")
        Tools.Printer.output("This game operates similarily to ZORK. Figure out the commands yourself or type HELP.")
        Tools.Printer.output("To begin, type start and press enter.")
        Tools.Printer.output("To exit, type quit and press enter.")

    def help(self):
        Tools.Printer.output("0++++++++++++++++++++++0")
        Tools.Printer.output("Git Gud Menu:")
        Tools.Printer.output("The following are valid commands:")
        Tools.Printer.output("'EXAMINE X', 'PRESENT X', 'LOOK', 'USE X', 'I', 'INVENTORY',")
        Tools.Printer.output("'GO TO X', 'SPEAK TO X', 'TALK TO X', 'SUDOKU'")
        Tools.Printer.output("That's it, figure everything out yourself numbskull. Now GIT GUD.")
        Tools.Printer.output("0++++++++++++++++++++++0")

    def quit(self):
        Tools.Printer.output("Until next time.")
        sys.exit()

    def showInv(self):
        self.inv.display()

    def death_via_grue(self):
        #add more rooms. btw I don't think this is working properly.
        if self.currentRoom == "ROOM3":
            Tools.Printer.output("Suddenly, a GRUE arises from the darkness and consumes you.")
            Tools.Printer.output("Congratulations, you are now dead.")
            sys.exit()

    def sudoku(self):
        Tools.Printer.output("You have brought shame upon yourself and your family.")
        Tools.Printer.output("Thus, you pull out an knife and carve a Sudoku puzzle unto your torso.")
        Tools.Printer.output("Within minutes you bleed to death. Good job!")
        self.quit()

    def ending(self):
        pass
#=======================================#

    def presentItem1(self):
        if self.currentRm == "CASTLE":
            if self.inventory.hasItem("SWORD"):
                Tools.Printer.output("You present the sword to the Duke. He is very pleased and gives you a large sum of gold.")
                Inv.Inventory.removeItems("SWORD")
                Inv.Inventory.addItems("SACKOFGOLD")
            else:
                Tools.Printer.output("You don't have this item on you! How could you present it to the duke?")
                return

    def presentItem2(self):
        if self.currentRm == "TAVERN2":
            if self.inventory.hasItem("RING"):
                Tools.Printer.output("You present the ring to the pretty barmaid. She is estatic and accepts your proposal.")
                Tools.Printer.output("She then leads you to a secluded room to 'cement' the new relationship.")
                self.ending()
            else:
                Tools.Printer.output("You are still empty handed! What are you doing?")
                return
