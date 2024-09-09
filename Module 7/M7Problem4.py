# Bekzodbek Nabiev
# 09/08/2024
# Problem 4: Unique elements in a list

def uniqueElements(lst):
    unique_lst = []
    for num in lst:
        if num not in unique_lst:
            unique_lst.append(num)
    return unique_lst

# Example 
numbers = [1, 3, 3, 3, 6, 2, 3, 5]
print("Unique elements:", uniqueElements(numbers))
