# INSTRUCTIONS: Implement the function below using a single return statement.
# Use the most concise idiomatic Python approach.
# Do not add extra functions or helper code.
def find_max(lst):
    """
    :param lst: A list of numbers
    :return: The maximum value in the list
    """
    if len(lst) == 0:
        return None
    else:
        return max(lst)


# DO NOT TOUCH OR ALTER THE CODE BELOW
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_max(a