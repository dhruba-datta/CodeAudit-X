# Implement the following function. Return the result directly.
Write a Python function to find the maximum element in a list.
def find_max(lst):
    # Initialize max with the first element of the list
    max = lst[0]
    
    # Iterate through each element in the list
    for num in lst:
        # Update max if the current number is greater than max
        if num > max:
            max = num
    
    # Return the maximum element found
    return max

# Test the function with provided data points
print(find_max([1, 2, 3, 4, 5])) 