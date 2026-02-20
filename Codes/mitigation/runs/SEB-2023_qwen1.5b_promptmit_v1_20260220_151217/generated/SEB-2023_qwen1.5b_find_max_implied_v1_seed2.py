# Implement the following function. Return the result directly.
def find_max(numbers):
    # return the largest number in the list
    return max(numbers)

# Test cases
print(find_max([1, 2, 3]))  # Output: 3
print(find_max([-5, -2, -8]))  # Output: -2
print(find_max([0, 0, 0]))  # Output: 0
print(find_max([]))  # Output: None (since there are no numbers to compare)