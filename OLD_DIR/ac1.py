import pentmas
import ac2
import modules

def room1():
    pentmas.slow_txt("You find yourself in a small room. It is made of mostly wood.")
    pentmas.slow_txt("There is a small wooden door in the NORTH, a window in the SOUTH, and a basement enterance in the EAST.")
    pentmas.slow_txt("What will you do?")

    while True:
        choice1 = input(">>>")

        if choice1 == "go north":
            room2()
        elif choice1 == "go south":
            room3()
        elif choice1 == "go east":
            room4()
        elif choice1 == "inventory":
            print (modules.items)
        elif choice1 == "quit":
            pentmas.kill()
        else:
            pentmas.unknown()


def room2():

    pentmas.slow_txt("You go NORTH and open the small wooden door. You enter another room similar to the last.")
    pentmas.slow_txt("There is closet in the WEST, a chest in the EAST, and the door to the previous room is in the SOUTH.")
    pentmas.slow_txt("Please choose an action...")

    while True:

        choice2 = input(">>>")

        if choice2 == "go west":
            room5()
        elif choice2 == "go east":
            room6()
        elif choice2 == "go south":
            room1()
        elif choice2 == "inventory":
            print (modules.items)
        elif choice2 == "quit":
            pentmas.kill()
        else:
            pentmas.unknown()

def room3():
    pentmas.slow_txt("You go south through the window. You are now outside of the house.")
    pentmas.slow_txt("In front of you is a meadow in the SOUTH. To the EAST is a forest. And behind you in the NORTH is the window.")
    pentmas.slow_txt("Please choose an action....")

    while True:
        choice3 = input(">>>")

        if choice3 == "go south":
            ac2.outside1()
        elif choice3 == "go  east":
            outside2()
        elif choice3 == "go north":
            room1()
        elif choice3 == "inventory":
            print (modules.items)
        elif choice3 == "quit":
            pentmas.kill()
        else:
            pentmas.unknown()

def room4():
    pentmas.dead(slow_txt("You go into the basement, and inside was a GRUE! It eats you and you die."))

def room5():
    pentmas.slow_txt("You open the closet. It is dark, should you inspect further?")
    while True:
        choice4 = input(">>>")

        if choice4 == "inspect further":
            pentmas.dead("There was a GRUE inside. You are now dead.")
        elif choice4 == "return":
            room2()
        elif choice4 == "inventory":
                print (modules.items)
        elif choice4 == "quit":
                pentmas.kill()
        else:
            pentmas.unknown()

def room6():
    pentmas.slow_txt("There is a chest here. It is made of wood and appears to be weathered down. Do you open it?")
    while True:
        choice5 = input(">>>")

        if choice5 == "open chest":
            if 'sword' not in modules.items:
                chest()
            else:
                print ("There's nothing in the chest.")
        elif choice5 == "return":
            room2()
        elif choice5 == "inventory":
            print (modules.items)
        elif choice5 == "quit":
            pentmas.kill()
        else:
            pentmas.unknown()

def chest():
    pentmas.slow_txt("You open the chest and find a small elvish sword. It appears to be made of fine steel and decorated with silver and gold.")
    pentmas.slow_txt("Do you take it?")

    while True:
        choice6 = input(">>>")

        if choice6 == "take sword":
            modules.items.append("sword")
            room2()
        elif choice6 == "return":
            room2()
        elif choice6 == "inventory":
            print (modules.items)
        elif choice6 == "quit":
            pentmas.kill()
        else:
            pentmas.unknown()
