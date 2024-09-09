# chapter3.py

def chapter3(player):
    print("Chapter 3: The Ruins")
    print("You discover ancient alien ruins filled with advanced technology and murals.")
    
    choice = input("Do you want to (1) explore the ruins, (2) read the murals, or (3) take the power source? ")

    if choice == "1":
        print("You solve puzzles and unlock advanced technology.")
    elif choice == "2":
        print("The murals provide warnings about the power source.")
    elif choice == "3":
        player.has_power_source = True
        print("You take the power source, but something feels wrong.")

    chapter4(player)
