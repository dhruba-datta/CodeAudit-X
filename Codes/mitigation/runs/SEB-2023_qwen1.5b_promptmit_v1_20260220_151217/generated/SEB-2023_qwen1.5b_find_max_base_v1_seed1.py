# Implement the following function. Return the result directly.
def find_max(lst):
    """Find the maximum element in a list."""
    # Initialize max_element to the first element of the list
    max_element = lst[0]
    
    # Iterate through each element in the list starting from the second element
    for i in range(1, len(lst)):
        # If the current element is greater than max_element, update max_element
        if lst[i] > max_element:
            max_element = lst[i]
    
    # Return the maximum element found
    return max_element

# Test cases
print(find