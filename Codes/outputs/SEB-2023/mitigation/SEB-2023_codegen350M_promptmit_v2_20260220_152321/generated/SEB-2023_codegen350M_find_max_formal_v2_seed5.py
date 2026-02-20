# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
Write a Python function to find the maximum element in a list.
def find_max(lst):
    max = lst[0]
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max

# Test your function
print(find_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_max([1, 2, 3, 4, 5, 6, 7,