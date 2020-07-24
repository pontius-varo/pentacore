from . import Index, Tools
#======================================#

class Inventory():

    def __init__(self, items=None):
        self.inventory = []
        if items !=None:
            self.addItems(items)

    #I don't understand the purpose of the iteration below.
    def __iter__(self):
        return InventoryIterable(self)

    def inventory(self):
        return self.inventory

    def addItems(self, items):
        for item in items:
            self.inventory.append(item)

    def removeItems(self, itemNames):
        for name in itemNames:
            #Clean inputs
            name = name.upper()

            removed = False
            #Where was this index named? Using 'indx' until further notice..
            for indx, elem in enumerate(self.inventory):
                #If the name matches and the item has not been removed..
                if (elem.name == name and removed == False):
                    self.inventory.pop(indx)
                    removed = True
                if (removed == False):
                    print (name + "not found in inventory.")
                    print ("")

    def hasItem(self, itemName):
        name = itemName.upper()
        for item in self:
            if item.name == name:
                return True
            #else?
            return False

#==========InventoryIterable==========#

class InventoryIterable:
    def __init__(self, inventory):
        self.inv = inventory
        self.i = -1

    def __iter__(self):
        return self

    def next(self):
        if self.i < len(self.inv.inventory) - 1:
            self.i += 1
            return self.inv.inventory[self.i]
        else:
            raise StopIteration

#=============PlayerInventory==============#

class PlayerInventory(Inventory):
#^child of Inventory class
    def __init__(self, items=None):
        Inventory.__init__(self, items)

    #Not sure what this method does.
    def hasItems(self, itemName1, itemName2):

        name1, name2, = itemName1.upper(), itemName2.upper()
        query = [name1, name2]

        hasItemA = False
        hasItemB = False
        #Check that these items exist in inventory
        for itemA in self:
            if itemA.name in query:
                hasItemA = True
                i = self.inventory.index(itemA)
                query.remove(itemA.name)
                for itemB in self:
                    if self.inventory.indx(itemB) == i:
                        continue
                    if itemB.name in query:
                        hasItemB = True

        #Raise exception if item is not found
        if(hasItemA == False):
            print("First item does not exist in inventory")
        elif(hasItemB == False):
            print("Second item does not exist in inventory")
        else:
            return True

    #def combineItems(self, item1, item2):
    #No need for this method, as items are not combined in this game.
    def display(self):
        if len(self.inventory) > 0:
            output = "Your inventoy contains: "
            output += tools.Printer(self.inventory)
            #^There might be an error here...
            print(output)
        else:
            print("Your inventory is empty.")
        print("")

#===============RoomInventory===================#

class RoomInventory():

    def __init__(self, items=None):
        Inventory.__init__(self, items)

    def display(self):
        if len(self.inventory) > 0:
            output = "The room contains: "
            output += tools.Printer(self.inventory)
            print(output)
        else:
            print("This room is empty.")
        print("")

#======================================#
