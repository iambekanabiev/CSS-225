# chapter1.py

def chapter1(player):
    print("Chapter 1: Crash")
    print(f"As {player.name} bursts through the atmosphere, they brace for impact.")
    print("You wake up near your ship wreckage, disoriented but alive.")
    
    choice = input("Do you want to (1) examine the wreckage, (2) scavenge the area, or (3) explore the surroundings? ")

    if choice == "1":
        print("You find a damaged communication device and some supplies.")
    elif choice == "2":
        print("You collect alien flora that may be used for healing.")
    elif choice == "3":
        print("You encounter non-aggressive alien creatures.")
    
    next_choice = input("Do you want to (1) attempt repairs on the ship or (2) explore the environment? ")
    
    if next_choice == "1":
        print("You begin to repair the ship but it's too damaged. You decide to explore.")
    chapter2(player)
