from ai import speakWithFrank
from ai import speakWithAlien
from ai import speakWithOldLady
import random


def main():
    x, y = 0, 0
    visited_locations = set()
    inventory = set()
    mapStatus = set()
    quitGame = set()
    messages = [
                "What did you say?",
                "Come again?",
                "Try that again.",
                "Sorry, one more time.",
                "Huh?"
            ]

    print("----------------------------------------------------------------------------------")
    print("               --  --  --  --  --  --  --  --  --  --  --  --")
    print("                   _____")                                  
    print("                  (, /  |    /)")                           
    print("                    /---|  _(/ _ _   _ __  _/_     __   _") 
    print("                 ) /    |_(_(_ (/___(/_/ (_(__(_(_/ (__(/_")
    print("                (_/") 
    print("               --  --  --  --  --  --  --  --  --  --  --  --")                                    
    print("----------------------------------------------------------------------------------")
    print("Welcome to Adventure! [type 'north', 'south', 'east', 'west', for directions]\n")
    print("You wake up in a strange forest surrounded by huge trees, the sun is peeking through.")

    while True:
        command = input("What do you do? ").strip().lower()

        if command in ('quit'):        #if player wants to quit game
            print('Are you sure you want to quit the game?')
            quitGame.add("imSure")

        if command in ('yes', 'y'):
            if "imSure" in quitGame:
                print("\nThank you for playing!\n")
                break
            else:
                print("Huh?")

        if command in ('grab', 'take', 'pick up'):       #player grabbing an item
            if (x, y) == (1, 2):
                print("You grabbed the torch.")
                inventory.add("torch")
            elif (x, y) == (5, 1):
                print("You picked up the machete.")
                inventory.add("machete")
            elif (x, y) == (11, 6):
                print("You looked under the rock and found a key!")
                inventory.add("key")

        if command in ('go in', 'enter', 'open door', 'open', 'go', 'go through'):
            if (x, y) == (2, 2):
                y += 1
                print("Now inside of the dimly lit cabin, you see a content man in the corner sitting in his rocking chair.")
            elif (x, y) == (0, 0):
                if "endgame" in inventory:
                    y -= 1
                    print("You start walking down the mysterious path, confused on where you are.")
                else:
                    print("Y O U  A R E  T O O  E A R L Y")

        if command in ('cut', 'trim', 'make path'):
            if (x, y) == (4, 4):
                mapStatus.add("northForest")
                print("You cut the trees and made a path.")
    
        if command in ('exit', 'leave', 'leave cabin', 'leave house'):
            if (x, y) == (2, 3):
                y -= 1
                print("You are now back outside.")

        if command in ('talk', 'speak', 'chat', 'frank', 'talk to frank', 'talk with frank', 'talk with old lady', 'talk to old lady', 'talk to alien', 'talk with alien'):
            if (x, y) == (0, 4):
                speakWithFrank()
            elif (x, y) == (4, 14):
                speakWithOldLady()
            elif (x, y) == (12, 1):
                speakWithFrank()

        if command in ('north', 'n'):         #player moving north

            northForestTrees = [(-1, 5), (3, 5), (5, 5), (6, 5)]
            northForestCabin = [(0, 5), (1, 5), (2, 5)]

            northForestMovement = [(0, 1), (-1, 2), (-1, 4), (4, 1), (6, 1), (4, 2), (5, 2), (5, 4), (6, 4)]
            northForestMovement2 = [(1, 1), (2, 1), (3, 1), (3, 3), (4, 3), (6, 3), (3, 4)]

            if (x, y + 1) in northForestMovement:
                y += 1
                print("You walk north.")
            elif (x, y + 1) in northForestMovement2:
                y += 1
                print("You walk north frolicing through the grass.")
            elif (x, y + 1) in northForestTrees:
                print("The thick forest blocks your path.") 
            elif (x, y + 1) in northForestCabin:
                print("The cabin walls block your path.")
            elif (x, y + 1) == (0, 2):
                y += 1
                print("You continue north until you find a cabin, looking in the window you see a dimly lit room with a man inside.")
            elif (x, y + 1) == (1, 2):
                y += 1
                print("You are outside the cabin, it has a burnt out torch attached to the outside.")
            elif (x, y + 1) == (2, 2):
                y += 1
                print("Moving north you find the door to the cabin.")
            elif (x, y + 1) == (0, 3):
                print("You cannot walk through the window.")
            elif (x, y + 1) == (1, 3):
                print("You cannot walk through the wall.")
            elif (x, y + 1) == (2, 3):
                print("You cannot walk through the door.")
            elif (x, y + 1) == (-1, 1):
                y += 1
                print("You move north, encountering a little sleeping cat. He just sits there and looks cute.")
            elif (x, y + 1) == (-1, 3):
                y += 1
                if "waterfall" in inventory:
                    print("It seems there is an opening that wasn't here before...")
                else:
                    print("You walk north.")
            elif (x, y + 1) == (3, 2):
                y += 1
                print('You move north. There is a tree that has a heart carved in the bark with an "F + R" on the inside.')
            elif (x, y + 1) == (5, 1):
                y += 1
                print("You come across a log after you move north. It appears to have a machete loosely stuck in the wood.")
            elif (x, y + 1) == (5, 3):
                y += 1
                print("You move north and spot two trees with a swing for two, how cute.")
            elif (x, y + 1) == (4, 4):
                y += 1
                if "machete" in inventory:
                    print("You move north. It seems you can cut some small trees to make a path.")
                else:
                    print("You move north.")
            elif (x, y + 1) == (4, 5):
                if "northForest" in mapStatus:
                    y += 1
                    print("You move into the path you made in the trees.")
                else:
                    print("The thick forest blocks your path.")
            elif (x, y + 1) == (2, 4):
                y += 1
                print("You move up into the room and look at the bookshelf in the corner of the room, everything looks well dusted.")
            elif (x, y + 1) == (1, 4):
                y += 1
                print("You move north in the room, there is a nice picture of an old man and an old woman, happily in love.")
            elif (x, y + 1) == (0, 4):
                y += 1
                print("You see Frank right in front of you, sitting on his rocking chair minding his own business.")
            


        if command in ('east', 'e'):      #player moving east

            eastForestTrees = [(7, 4), (7, 3), (7, 1), (7, 0)]

            eastForestMovement = [(0, 1), (1, 1), (2, 1), (3, 3), (4, 1), (4, 0), (5, 0), (6, 4), (6, 3), (6, 0)]
            eastForestMovement2 = [(1, 0), (2, 0), (4, 3), (4, 2), (3, 1), (3, 4), (5, 2), (5, 4), (6, 1)]

            if (x + 1, y) in eastForestMovement:
                x += 1
                print("You walk east striding through the grass.")
            elif (x + 1, y) in eastForestMovement2:
                x += 1
                print("You walk east.")
            elif (x + 1, y) in eastForestTrees:
                print("The thick forest blocks your path.")
            elif (x + 1, y) == (1, 2):
                x += 1
                print("You are in front of the cabin, it has a burnt out torch attached to the outside.")
            elif (x + 1, y) == (2, 2):
                x += 1
                print("You come across the door to the cabin.")
            elif (x + 1, y) == (0, 3):
                print("You cant walk into the cabin wall")
            elif (x + 1, y) == (0, 4):
                print("You cant walk into the cabin wall")
            elif (x + 1, y) == (0, 2):
                x += 1
                print("You move east, there is a window. Looking inside reveals a dimly lit room with a man inside.")
            elif (x + 1, y) == (0, 0):
                x += 1
                if "endgame" in inventory:
                    print("There seems to be a path here that opened up. Guess I didnt see it the first time.")
                else:
                    print("You walk east.")
            elif (x + 1, y) == (3, 0):
                x += 1
                print("You move east. You stop and see a big tree with a friendly face on it, looks like someone likes decorating.")
            elif (x + 1, y) == (3, 2):
                x += 1  
                print('You move east. There is a tree that has a heart carved in the bark with an "F + R" on the inside.')
            elif (x + 1, y) == (5, 1):
                x += 1
                print("You come across a log after you move east. It appears to have a machete loosely stuck in the wood.")
            elif (x + 1, y) == (4, 4):
                x += 1
                if "machete" in inventory:
                    print("You move east. It seems you can cut some small trees to make a path.")
                else:
                    print("You walk east striding through the grass.")
            elif (x + 1, y) == (5, 3):
                x += 1
                print("You move east and spot two trees with a swing for two, how cute.")
            

        if command in ('south', 's'):        #player moving south

            southForestTrees = [(-1, -1), (1, -1), (2, -1), (3, -1), (4, -1), (5, -1), (6, -1)]

            southForestMovement = [(-1, 2), (-1, 0),  (3, 1), (4, 1), (1, 0), (5, 2), (4, 2), (4, 3), (3, 3)]
            southForestMovement2 = [(0, 1), (1, 1), (5, 0), (6, 0), (6, 3), (2, 1), (2, 0), (4, 0), (6, 1)]

            if (x, y - 1) in southForestMovement:
                y -= 1
                print("You walk south through some grass.")
            elif (x, y - 1) in southForestMovement2:
                y -= 1
                print("You walk south.")

            elif (x, y - 1) in southForestTrees:
                print("The thick forest blocks your path.")

            elif (x, y - 1) == (0, -1):
                if "endgame" in inventory:
                    print("There seems to be a path here that opened up. Guess I didnt see it the first time.")
                else:
                    print("The thick forest blocks your path.")
            elif (x, y - 1) == (2, 2):
                print('"The door is closed behind you, would you like to leave?" says the old man.')
            elif (x, y - 1) == (-1, 3):
                y -= 1
                if "waterfall" in inventory:
                    print("There seems to be an opening that wasnt here before...")
                else:
                    print("You walk south through the grass.")
            elif (x, y - 1) == (3, 0):
                y -= 1
                print("You move south. You stop and see a big tree with a friendly face on it, looks like someone likes decorating.")
            elif (x, y - 1) == (3, 2):
                y -= 1
                print('You move south. There is a tree that has a heart carved in the bark with an "F + R" on the inside.')
            elif (x, y - 1) == (5, 3):
                y -= 1
                print("You move south. You come across two trees with a swing for two, how cute.")
            elif (x, y - 1) == (5, 1):
                y -= 1
                print("You come across a log after you move south. It appears to have a machete loosely stuck in the wood.")
            elif (x, y - 1) == (-1, 1):
                y -= 1
                print("You move south, encountering a little sleeping cat. He just sits there and looks cute.")


        
            

main()