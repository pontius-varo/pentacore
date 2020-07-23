import textwrap
from sys import exit
from time import sleep

class Printer():

    def __init__(self):
        pass

    @staticmethod #I forget, what is the purpose of a static method?
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
        for x in txt:   #cycle through the text one character at a time
            print(x, end='', flush=True)
            sleep (0.1) # switch to one after debugging.
        print()
