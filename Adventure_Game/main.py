# main.py

from chapter1 import chapter1
from chapter2 import chapter2
from chapter3 import chapter3
from chapter4 import chapter4
from chapter5 import chapter5

class Player:
    def __init__(self, name):
        self.name = name
        self.has_power_source = False
        self.allied_with_guardian = False

def start_game():
    print("Welcome to the Adventure Game!")
    name = input("Enter your character's name: ")
    player = Player(name)
    
    # Start the first chapter
    chapter1(player)

if __name__ == "__main__":
    start_game()
