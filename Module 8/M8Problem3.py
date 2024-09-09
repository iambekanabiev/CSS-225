# Bekzodbek Nabiev
# 09/08/2024
# This program checks if the value 5 is present in a given list.

def check_five_in_list():
    my_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

    if 5 in my_list:
        print("The value 5 is in the list.")
    else:
        print("The value 5 is not in the list.")

# Call the function
check_five_in_list()
