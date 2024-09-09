# Bekzodbek
# 09/08/2024
# Problem 4: Create a while loop that adds numbers divisible by 10 from 0 to 50 into a list

tens = []  #  empty list
counter = 0  #  counter at 0

while counter <= 50:
    if counter % 10 == 0:  # Check if the counter is divisible by 10
        tens.append(counter)  
    counter += 1  

print(tens)  # Print the list to confirm
