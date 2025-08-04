def change_set_value_by_index(my_set, index, new_value):
    # Sets are unordered, so they don't have indices.
    # To change a value at a conceptual "position", we must first convert the set to a list.
    my_list = list(my_set)

    # Use a try-except block to handle cases where the index is out of bounds.
    try:
        # Check if the index is valid.
        if 0 <= index < len(my_list):
            # Modify the value in the list at the specified index.
            my_list[index] = new_value
            # Convert the list back to a set. This will remove any duplicate values
            # that might have been introduced.
            return set(my_list)
        else:
            print(f"Error: Index {index} is out of range for the set.")
            return my_set
    except IndexError:
        # This catch is technically redundant due to the if statement, but
        # is good practice for robust code.
        print(f"Error: Index {index} is out of range.")
        return my_set



# Define the initial set
initial_set = {10, 20, 30, 40, 50}
print(f"Original Set: {initial_set}")

index_to_change = 2
value_to_add = 99

modified_set = change_set_value_by_index(initial_set, index_to_change, value_to_add)

print(f"Modified Set: {modified_set}")
