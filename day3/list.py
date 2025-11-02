# 1. Creating a list
my_list = [1, 2, 3, 'apple', 4.5, True]  
another_list = list((1, 2, 3)) 
empty_list = []  
print("1. Original list:", my_list)

# 2. Accessing elements (Indexing and Slicing)
print("\n2. Accessing elements:")
print("First element:", my_list[0])  
print("Last element:", my_list[-1])  
print("Sliced (elements 1 to 3):", my_list[1:4]) 
print("Sliced from start to 3:", my_list[:3])  
print("Sliced from 3 to end:", my_list[3:])  

# 3. Length of the list
print("\n3. Length of the list:", len(my_list))

# 4. Adding elements
print("\n4. Adding elements:")
my_list.append(6)
print("After append(6):", my_list)
my_list.insert(2, 'orange')  # Insert at specific position (index 2)
print("After insert('orange' at index 2):", my_list)
my_list.extend([7, 8])  # Add multiple elements from another list
print("After extend([7, 8]):", my_list)

# 5. Removing elements
print("\n5. Removing elements:")
my_list.remove('apple')  # Remove by value (first occurrence)
print("After remove('apple'):", my_list)
popped_element = my_list.pop(1)  # Remove by index and return the element
print("After pop(1) (removed element:", popped_element, "):", my_list)
del my_list[0]  # Delete by index (removes the first element)
print("After del my_list[0]:", my_list)
my_list.clear()  # Remove all elements
print("After clear():", my_list)

# Re-create the list for further operations
my_list = [4, 2, 8, 1, 5, 3]

# 6. Modifying elements
print("\n6. Modifying elements:")
my_list[0] = 10  # Change an element by index
print("After modifying index 0 to 10:", my_list)

# 7. Sorting and reversing
print("\n7. Sorting and reversing:")
sorted_list = sorted(my_list)  # Returns a new sorted list
print("Sorted list:", sorted_list)
my_list.sort()  # Sorts the list in place (ascending)
print("After sort():", my_list)
my_list.sort(reverse=True)  # Sorts in descending order
print("After sort(reverse=True):", my_list)
my_list.reverse()  # Reverses the list in place
print("After reverse():", my_list)

# 8. Membership testing
print("\n8. Membership testing:")
print(2 in my_list)  # Check if an element exists
print(10 not in my_list)  # Check if an element does not exist

# 9. Iteration
print("\n9. Iteration:")
for item in my_list:
    print(item, end=' ')  # Loop through elements
print()  # New line
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

# 10. List comprehensions (Creating a new list based on existing one)
print("\n10. List comprehensions:")
squares = [x ** 2 for x in my_list]
print("Squares of elements:", squares)
even_numbers = [x for x in my_list if x % 2 == 0]
print("Even numbers:", even_numbers)

# 11. Other useful methods
print("\n11. Other methods:")
my_list = [1, 2, 2, 3, 4]  # Reset for demonstration
print("Count of 2:", my_list.count(2))  # Count occurrences
print("Index of 3:", my_list.index(3))  # Find index of first occurrence
my_list_copy = my_list.copy()  # Create a shallow copy
print("Copied list:", my_list_copy)

# 12. Joining lists
print("\n12. Joining lists:")
joined_list = my_list + [5, 6]  # Concatenate
print("Joined list:", joined_list)

# 13. Converting to other types
print("\n13. Converting to other types:")
my_tuple = tuple(my_list)  # To tuple
print("As tuple:", my_tuple)
my_set = set(my_list)  # To set (removes duplicates)
print("As set:", my_set)

print("\nAll operations completed!")
