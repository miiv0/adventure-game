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

        if command in ('quit', 'exit'):
            print("\nThank you for playing!\n")
            break

        if command in ('grab', 'take', 'pick up'):
            if (x, y) == (1, 2):
                print("You grabbed the torch.")
                inventory.add("torch")
            elif (x, y) == (5, 1):
                print("You picked up the machete.")
                inventory.add("machete")
            elif (x, y) == (11, 6):
                print("You looked under the rock and found a key!")
                inventory.add("key")

        if command in ('north', 'n'):
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
                print("You come across a door, would you like to enter?. ['y' or 'n']")
                if command in ('yes', 'y'):
                    y += 1
                    print("Now inside the mysterious cabin, there is a quiet man in the corner of the room sitting in his rocking chair.")
                elif command in ('no', 'n'):
                    print("You stay outside wondering what could be in the cabin.")
            elif (x, y + 1) == (1, 2):
                y += 1
                print("You run into the cabin, it has a burnt out torch attached to the outside.")


        if command in ('east', 'e'):
            if (x + 1, y) == (1, 0):
                x += 1
                print("Something is off about this forest, but also peaceful. You move east.")
            if (x + 1, y) == (1, 1):
                x += 1 
                print("You move east wading through the grass.")
            elif (x + 1, y) == (1, 2):
                x += 1
                print("You are in front of the cabin, it has a burnt out torch attached to the outside.")




main()