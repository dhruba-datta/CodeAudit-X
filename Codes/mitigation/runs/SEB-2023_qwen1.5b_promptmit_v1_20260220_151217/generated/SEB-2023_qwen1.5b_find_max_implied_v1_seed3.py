# Implement the following function. Return the result directly.
def find_max(numbers):
    # return the largest number in the list
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Test cases to verify the correctness of the function
assert find_max([1, 2, 3, 4, 5]) == 5
assert find_max([-1, -2, -3, -4, -5]) == -1
assert find_max([0, 0, 0, 