from sys import exit
from time import sleep

def slow_txt(txt):
    for x in txt:   #cycle through the text one character at a time
        print(x, end='', flush=True)
        sleep (0.1) # switch to one after debugging.
    print()

def dead(why):
    slow_txt(why)
    exit(0)

def kill():
    slow_txt("Until next time.")
    exit(0)

def unknown():
    print ("I don't understand what that means.")

def end():
    print("Congratuations! A winner is you.")
    print("Your score was over 900000.")
    kill()
