import pentmas
import modules
import ac2


def mountain():
    pentmas.slow_txt("You follow the alternative trail and after many long hours you arrive at a mountain.")
    pentmas.slow_txt("The mountain looms above your head, it is dark and reachs towards the heavens above.")
    pentmas.slow_txt("To the north there appears to be some sort of stairway leading up the mountain, while to the west is the meadow you came from")
    pentmas.slow_txt("Please choose an action...")

    while True:
        choice1 = input(">>>")

        if choice1 == "go north":
            mountain2()
        elif choice1 == "go west":
            ac2.outside1()
        elif choice1 == "inventory":
            print (modules.items)
        elif choice1 == "quit":
            pentmas.kill()
        else:
            pentmas.unknown()

def mountain2():
    pentmas.slow_txt("You climb the stairway which takes you far up into the mountain. At the end of the trail there is a cave to the north.")
    pentmas.slow_txt("Behind you to the south is the area you came from. What will you do?")

    while True:
        choice2 = input(">>>")

        if choice2 == "go north":
            cave1()
        elif choice2 == "enter cave":
            cave1()
        elif choice2 == "go south":
            mountain()
        elif choice2 == "inventory":
            print (modules.items)
        elif choice2 == "quit":
            pentmas.kill()
        else:
            pentmas.unknown()

def cave1():
    pentmas.slow_txt("You enter the cave. It is dark and you are likely to be eaten by a grue.")
    pentmas.slow_txt("There are two paths in the cave, one leading to the left and another to the right. To the south of you is an exit.")
    pentmas.slow_txt("What will you do?")

    while True:
        choice3 = input(">>>")

        if choice3 == "go left":
            pentmas.dead("You go left and encounter a GRUE! You are dead.")
        elif choice3 == "go right":
            if 'ring' not in modules.items:
                cave2()
            else:
                'You already went that way and took the ring you fool! There\'s nothing left for you there.'
        elif choice3 == "go south":
            mountain2()
        elif choice3 == "inventory":
            print (modules.items)
        elif choice3 == "quit":
            pentmas.kill()
        else:
            pentmas.unknown()

def cave2():
    pentmas.slow_txt("You go down the left path and reach a dead end. On the way however, you step on what feels like a small ring.")
    pentmas.slow_txt("Obvious exit is to the north. What will you do?")

    while True:
        choice4 = input(">>>")

        if choice4 == "take ring":
            modules.items.append("ring")
            cave1()
        elif choice4 == "go north":
            cave1()
        elif choice4 == "inventory":
            print (modules.items)
        elif choice4 == "quit":
            pentmas.kill()
        else:
            pentmas.unknown()
    
