# chapter2.py

def chapter2(player):
    print("Chapter 2: The Unseen")
    print("You stumble upon a hidden alien village bustling with life.")
    
    choice = input("Do you want to (1) attempt to communicate, (2) gather information, or (3) help the villagers? ")
    
    if choice == "1":
        print("The villagers seem cautious, but a few are willing to talk.")
    elif choice == "2":
        print("You learn about ancient technology on this planet.")
    elif choice == "3":
        print("You help repair a structure and earn the villagers' trust.")
    
    next_choice = input("Do you want to (1) stay and learn or (2) leave the village? ")
    
    if next_choice == "1":
        print("You stay and learn from the villagers.")
    chapter3(player)
