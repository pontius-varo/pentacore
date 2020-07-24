import textwrap
from sys import exit
from time import sleep
from . import Index

class Printer():

    def __init__(self):
        pass

    @staticmethod
    def output(string, width=80):
        lines = []
        splitStr = string.splitlines()
        for line in splitStr:
            for l in textwrap.wrap(line,width):
                lines.append(l)
            lines.append("")

        for line in lines:
            Printer.miniprint(line)


    def miniprint(txt):
        for x in txt:
            #cycle through the text one character at a time
            print(x, end='', flush=True)
             # switch to .1 after debugging.
            sleep (0.0)
        print()

#=====Item======#
class Item():

    name = None
    desc = None

    def __init__(self, name):

        validItem = False
        #The following checks to see if an item is valid (that is to say, inside the array located in index.py)
        for key in index.items:
            if key == name.upper():
                self.name = key
                self.desc = index.items[key]["DESC"]
                validItem = True
                #if all the conditions above are met, then the item is valid
            if(validItem == False):
                #Invalid item
                raise Exception("Attempt to instantiate an invalid item!")
                del self

    def examine(self):
        return(self.desc)

    def __str__(self):
        return self.name

#Less is more!
