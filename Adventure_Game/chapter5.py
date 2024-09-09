# chapter5.py

def chapter5(player):
    print("Chapter 5: The Return")
    print("You return to the ship, ready to make your final decision.")
    
    if player.has_power_source:
        print("You have the power source from the ruins.")
        choice = input("Do you want to (1) use the alien power source or (2) use the ship's original systems? ")
        
        if choice == "1":
            print("You use the alien technology, but the ship behaves strangely.")
        else:
            print("You decide to use the ship’s original systems.")
    
    if player.allied_with_guardian:
        print("The guardian helps you pilot the ship.")
    
    print("You trigger the launch sequence and escape the planet.")
    print(f"{player.name}'s journey comes to an end, but the mysteries of the planet remain.")
