#Bekzodbek
# 09/08/2024

import random

# Module for exploring the wreckage
def explore_wreckage():
    print("Elon examines the wreckage of the ship.")
    items_found = ["damaged communication device", "emergency supplies", "ship log"]
    found_item = random.choice(items_found)
    print(f"Elon found: {found_item}")
    return found_item

# Module for scavenging the area
def scavenge_area():
    print("Elon searches the surrounding area for useful materials.")
    materials = ["healing herbs", "alien plants", "strange crystals"]
    collected_material = random.choice(materials)
    print(f"Elon collected: {collected_material}")
    return collected_material

# Module for encountering creatures
def encounter_creature():
    creatures = ["small, non-aggressive alien creatures", "glowing insects", "mysterious shadow"]
    creature = random.choice(creatures)
    print(f"Elon encounters: {creature}")
    action = input("Do you approach or observe from a distance? (approach/observe): ")
    
    if action == "approach":
        print(f"You cautiously approach the {creature}. They seem harmless.")
    else:
        print(f"You observe the {creature} from a safe distance. It disappears into the foliage.")
    return creature

# Module for deciding whether to repair the ship or explore further
def decision():
    print("Elon faces a choice: Attempt to repair the ship or explore the environment.")
    choice = input("Do you want to repair the ship or explore further? (repair/explore): ")
    
    if choice == "repair":
        print("Elon begins repairing the ship.")
        return "repair"
    else:
        print("Elon decides to explore the environment further.")
        return "explore"
