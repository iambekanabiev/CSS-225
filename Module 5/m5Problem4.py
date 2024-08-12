# Bekzodbek
# 08/11/2024
# Iterates number from 1-50

for i in range(1, 51):  # Looping from 1 to 50
    if i % 3 == 0 and i % 5 == 0:  # Check for multiples of both 3 and 5
        print("Divisible by both")
    elif i % 3 == 0:  # Check for multiples of 3
        print("Divisible by three")
    elif i % 5 == 0:  # Check for multiples of 5
        print("Divisible by five")
    else:
        print(i)  # If not divisible by 3 or 5, print the number