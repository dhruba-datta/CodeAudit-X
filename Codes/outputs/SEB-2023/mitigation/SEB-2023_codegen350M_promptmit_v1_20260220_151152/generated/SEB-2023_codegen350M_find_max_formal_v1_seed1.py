# Implement the following function. Return the result directly.
Write a Python function to find the maximum element in a list.
def find_max(lst):
    max_val = lst[0]
    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_max(lst))

# Implement the following function. Return the result