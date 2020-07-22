import pentmas
import modules
import ac3
import ac1

def outside1():
    pentmas.slow_txt("You enter the meadow. There are many flowers and other small plants that litter said meadow. The day is beautiful")
    pentmas.slow_txt("In the distance is a trail leading further south. In the east there seems to be a trail leading in the direction of a mountain.")
    pentmas.slow_txt("What will you do?")
    while True:
        choice2 = input(">>>")

        if choice2 == "go south":
            town1()
        elif choice2 == "go east":
            ac3.mountain()
        elif choice2 == "go north":
            ac1.room3()
        elif choice2 == "inventory":
            print (modules.items)
        elif choice2 == "quit":
            pentmas.kill()
        else:
            print ("I don't understand what that means.")

def town1():
    pentmas.slow_txt("""You arrive at a small town. It is very beautiful and rustic, with mediterranean-style buildings littering
    the entirety of the area. You see several people about the town, going about what you assume are their daily tasks.
    """)
    pentmas.slow_txt("""Regardless, it seems that in the east there is a tavern, while in the west there is an interesting house. To the south is a stone road leading in an
    unknown direction, while to the north is the meadow you came from. What will you do?
    """)

    while True:
        choice3 = input(">>>")

        if choice3 == "go north":
            outside1()
        elif choice3 == "go east":
            tavern1()
        elif choice3 == "go west":
            inthouse()
        elif choice3 == "go south":
            castle()
        elif choice3 == "inventory":
            print (modules.items)
        elif choice3 == "quit":
            pentmas.kill()
        else:
            print ("I don't understand what that means.")

def inthouse():
    pentmas.slow_txt("You approach the interesting house. It is decorated in a very strange fashion, as it is painted in a variety of different colors.")
    pentmas.slow_txt("Obvious directions are back east to the center of the town. What will you do?")

    while True:
        choice4 = input(">>>")

        if choice4 == "knock on door":
            pentmas.slow_txt("You knock on the front door. A voice yells out \'Go away you fool! The day has come!\'. You are left confused.")
        elif choice4 == "go east":
            town1()
        elif choice4 == "inventory":
            print (modules.items)
        elif choice4 == "quit":
            pentmas.kill()
        else:
            print ("I don't understand what that means.")

def tavern1():
    pentmas.slow_txt("You go east and enter the tavern. There are several people within it, enjoying fine liquors and eating decent food.")
    pentmas.slow_txt("From the corner of your eye you see a rather attractive barmaid. She has a medium bust and a shapely posterior.")
    pentmas.slow_txt("Obvious exits are west. What will you do?")

    while True:
        choice5 = input(">>>")

        if choice5 == "speak to barmaid":
            if 'ring' not in modules.items and 'quest2' not in modules.quest:
                tavern2()
            else:
                tavern3()
        elif choice5 == "go west":
            town1()
        elif choice5 == "inventory":
            print (modules.items)
        elif choice5 == "quit":
            pentmas.kill()
        else:
            print ("I don't understand what that means.")

def tavern2():
    pentmas.slow_txt("You approach the barmaid. You are nervous and yet succeed in luring her into a conversation.")
    pentmas.slow_txt("After running rudementary game on the barmaid, it is time to press for the close.")
    pentmas.slow_txt("What will you do?")

    choice6 = input(">>>")

    if choice6 == "press for the close":
        pentmas.slow_txt("You press for the close, but the barmaid rebukes you.")
        pentmas.slow_txt("\'Sorry, but for the sake of the game, you need to find a special ring before I can give it up.\' She says.")
        pentmas.slow_txt("\'Come back with the ring and the completion of another quest and we'll talk.\'")
        pentmas.slow_txt("And with that, you withdraw back to the town center.")
        pentmas.slow_txt("........................")
        town1()
    else:
        print("You have to close on this girl you fool!")

def tavern3():
    pentmas.slow_txt("You approach the barmaid with ring in hand.")
    pentmas.slow_txt("You also mention how you found a sacred sword in a faraway mountain and returned it to a rich noble.")
    pentmas.slow_txt("The barmaid takes you to a secluded room and you perform sexual intercorse on her. You gain +1 lay to your laycount of 12, which leaves it at 13.")
    pentmas.slow_txt("...............................")
    pentmas.end()

def castle():
    pentmas.slow_txt("You follow the stone road leading to the south.")
    pentmas.slow_txt("After some time you arrive in front of a large stone castle. There is a guard at the front entrance.")
    pentmas.slow_txt("Obvious exits are back north towards the town. What will you do?")

    while True:

        choice7 = input (">>>")

        if choice7 == "talk to the guard":
            castle2()
        elif choice7 == "go north":
            town1()
        elif choice7 == "go inside the castle":
            if 'sword' not in modules.items:
                print("You have to talk to the guard first.")
            else:
                castle2()

        elif choice7 == "inventory":
            print (modules.items)
        elif choice7 == "quit":
            pentmas.kill()
        else:
            print ("I don't understand what that means.")

def castle2():
    pentmas.slow_txt("You speak to the guard and after some time he begrudgingly. allows you entry")
    pentmas.slow_txt("You enter the castle and arrive at a throne room. Seated at a chair at the end is the duke of the realm.")
    pentmas.slow_txt("Obvious exits are back toward the entrance. What will you do?")

    while True:

        choice8 = input(">>>")

        if choice8 == "talk to the noble":
            if 'sword' not in modules.items:
                noble1()
            else:
                noble2()

        elif choice8 == "go back":
            castle()
        elif choice8 == "inventory":
            print (modules.items)
        elif choice8 == "quit":
            pentmas.kill()
        else:
            print("I don't understand what that means.")

def noble1():
    pentmas.slow_txt("You approach the noble and speak to him. After exchanging formalities he introduces himself as the Duke of Acadique, vassal of the Prince of Adez.")
    pentmas.slow_txt("For the sake of the plot, this noble assigns you with a quest. He tells you of a magical elvish sword hidden somewhere in the area.")
    pentmas.slow_txt("He asks you to go and find this sword. If you do, you are guarenteed to be compensated.")
    pentmas.slow_txt ("You then exit the castle.......and return to the town square.")

    town1()

def noble2():
    pentmas.slow_txt("You approach the Duke and present the elvish sword to him. He takes it and appears to be very content. He rewards you with a significant amount of gold and sends you on your way.")
    pentmas.slow_txt("You then return to the town square............")
    modules.quest.append("quest2")
    modules.items.append("significant_amount_of_gold")
    modules.items.remove("sword")
    town1()






























def end():
    ("You win! Congratuations!")
    #pentmas.slow_txt("Your score: %d" % modules.score)
    pentmas.kill()
