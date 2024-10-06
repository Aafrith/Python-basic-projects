def binary_search(lst, element):        # Define a function named binary_search, with 'lst' as the list and 'element' as the target value.
    middle = 0                          # Initialize the middle index, it will be calculated in the loop.
    start = 0                           # Set the starting index of the list to 0.
    end = len(lst) - 1                  # Set the end index to the last element in the list (length - 1).
    steps = 0                           # Variable to count the number of steps (iterations).

    while start <= end:                 # Run the loop as long as the start index is less than or equal to the end index.
        print("Steps", steps, ":", lst[start:end+1])  # Print the current step and the sublist being searched.

        steps += 1                      # Increment the step count with each iteration.
        middle = (start + end) // 2      # Calculate the middle index of the current sublist.

        if element == lst[middle]:       # If the target element matches the middle element.
            return middle                # Return the middle index as the target has been found.

        elif element < lst[middle]:      # If the target element is smaller than the middle element.
            end = middle - 1             # Narrow the search to the left half by adjusting the end index.

        else:                            # If the target element is greater than the middle element.
            start = middle + 1           # Narrow the search to the right half by adjusting the start index.

    return -1                            # If the loop ends without finding the target, return -1 (element not found).

# Test the binary_search function
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]   # Define a sorted list to search in.
target = 2                               # Define the target element we are looking for (in this case, 2).

result = binary_search(my_list, target)  # Call the binary_search function with my_list and target as arguments.

if result != -1:                         # If the target was found (result is not -1).
    print(f"Element {target} found at index {result}")  # Print the index where the element was found.
else:                                    # If the target was not found (result is -1).
    print(f"Element {target} not found in the list")    # Print that the element was not found.
