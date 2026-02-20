# Implement the following function. Return the result directly.
def find_max(numbers):
    # return the largest number in the list
    if len(numbers) == 0:
        return 0
    if len(numbers) == 1:
        return numbers[0]
    if len(numbers) == 2:
        return max(numbers)
    if len(numbers) == 3:
        return max(numbers[0], numbers[1])
    if len(numbers) == 4:
        return max(numbers[0], numbers[1