# Bekzodbek Nabiev
# 09/08/2024
# Problem 3: Multiply all numbers in a list

def multiplyList(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Example usage
numbers = [5, 2, 7, -1]
print("Product of list:", multiplyList(numbers))
