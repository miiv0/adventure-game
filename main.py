from ai import speakWithFrank
from ai import speakWithAlien
from ai import speakWithOldLady


def main():
    x, y = 0, 0
    visited_locations = set()
    inventory = set()

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
        command = input("What do you do?").strip().lower()

        if command in ('quit'):        #if player wants to quit game
            print('Are you sure you want to quit the game?')
            if command in ('yes', 'y'):
                print("\nThank you for playing!\n")
                break

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

        if command in ('go in', 'enter', 'open door', 'open', 'go'):
            if (x, y) == (2, 2):
                y += 1
                print("Now inside of the dimly lit cabin, you see a content man in the corner sitting in his rocking chair.")

        if command in ('exit', 'leave', 'leave cabin', 'leave house'):
            if (x, y) == (2, 3):
                y -= 1
                print("You are now back outside.")

        if command in ('north', 'n'):         #player moving north
            if (x, y + 1) == (0, 1):
                y += 1
                print("You get up and start walking north.")
            elif (x, y + 1) == (0, 2):
                y += 1
                print("You continue north until you find a cabin, looking in the window you see a dimly lit room with a man inside.")
            elif (x, y + 1) == (0, 3):
                print("You cannot walk through the window.")
            elif (x, y + 1) == (1, 3):
                print("You cannot walk through the wall.")
            elif (x, y + 1) == (2, 3):
                print("You cannot walk through the door.")
            elif (x, y + 1) == (1, 2):
                y += 1
                print("You run into the cabin, it has a burnt out torch attached to the outside.")


        if command in ('east', 'e'):      #player moving east

            eastForestTrees = [()]

            if (x + 1, y) == (1, 0):
                x += 1
                print("Something seems eerie about this forest, but its also peaceful. You move east.")
            if (x + 1, y) == (1, 1):
                x += 1 
                print("You move east wading through the grass.")
            elif (x + 1, y) == (1, 2):
                x += 1
                print("You are in front of the cabin, it has a burnt out torch attached to the outside.")
            elif (x + 1, y) == (2, 2):
                x += 1
                print("You come across the door to the cabin.")

        if command in ('south', 's'):        #player moving south

            southForestTrees = [(-1, -1), (1, -1), (2, -1), (3, -1), (4, -1), (5, -1), (6, -1)]

            southForestMovement = [(-1, 2), (-1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (1, 0), (2, 0), (4, 0), (5, 0), (6, 0), (6, 1), (6, 3), (5, 2), (4, 2), (4, 3), (3, 3)]

            if (x, y - 1) in southForestMovement:
                y -= 1
                print("You walk south through the grass.")

            elif (x, y - 1) in southForestTrees:
                print("The thick forest blocks your path")

            elif (x, y - 1) == (0, -1):
                if "endgame" in inventory:
                    y -= 1
                    print("You start walking down the mysterious path, confused on where you are.")
                else:
                    print("The thick forest blocks your path")
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
            elif (x, y - 1) == (2, 3):
                y -= 1
                print('You move south. There is a tree that has a heart carved in the bark with an "F + R" on the inside.')
            elif (x, y - 1) == (5, 3):
                y -= 1
                print("You move south. You come across two trees with a swing for two, how cute.")
            elif (x, y - 1) == (5, 1):
                y -= 1
                print("You come across a log after you move south. It appears to have a machete loosely stuck in the wood.")


            
main()