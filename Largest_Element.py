def find_largest_element(lst):
    if not lst:
        return None  # Return None for an empty list

    largest = lst[0]  # Assume the first element is the largest

    for element in lst:
        if element > largest:
            largest = element

    return largest

# Example usage:
my_list = [3, 8, 1, 6, 9, 2, 5]
result = find_largest_element(my_list)

if result is not None:
    print(f"The largest element in the list is: {result}")
else:
    print("The list is empty.")
