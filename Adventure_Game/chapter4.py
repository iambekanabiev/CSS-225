# chapter4.py

def chapter4(player):
    print("Chapter 4: The Awakening")
    print("You activate the ancient technology and awaken a robotic guardian.")
    
    choice = input("Do you want to (1) fight the guardian, (2) communicate, or (3) disable it? ")

    if choice == "1":
        print("You engage in combat and defeat the guardian.")
    elif choice == "2":
        player.allied_with_guardian = True
        print("You successfully communicate with the guardian, and it becomes your ally.")
    elif choice == "3":
        print("You disable the guardian using a strategic puzzle.")
    
    chapter5(player)
