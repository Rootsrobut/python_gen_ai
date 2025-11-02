# Demonstrating higher-order functions with lists in Python

# Sample list to work with
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. map() - Applies a function to every item in the list
# It takes a function and an iterable, and returns a map object (which you can convert to a list).
def square(x):
    return x ** 2  # Simple function to square a number

mapped_result = list(map(square, numbers))  # Apply square to each element
print("1. Using map() to square numbers:", mapped_result)

# You can also use a lambda function (anonymous function) with map()
mapped_lambda_result = list(map(lambda x: x * 2, numbers))  # Double each number
print("Using map() with lambda to double numbers:", mapped_lambda_result)

# 2. filter() - Filters the list based on a function that returns True/False
# It returns an iterator with only the elements that pass the test.
def is_even(x):
    return x % 2 == 0  # Check if a number is even

filtered_result = list(filter(is_even, numbers))  # Filter even numbers
print("2. Using filter() for even numbers:", filtered_result)

# With lambda:
filtered_lambda_result = list(filter(lambda x: x > 5, numbers))  # Filter numbers greater than 5
print("Using filter() with lambda for numbers > 5:", filtered_lambda_result)

# 3. sorted() - Sorts the list, and you can pass a key function for custom ordering
# The key function is a higher-order function example, as it defines how to sort.
fruits = ['apple', 'Banana', 'cherry', 'Date', 'elderberry']

# Basic sorting (case-sensitive by default)
sorted_fruits = sorted(fruits)  # Sorts alphabetically
print("3. Basic sorted() on fruits:", sorted_fruits)

# Using a key function to sort case-insensitively
def ignore_case(s):
    return s.lower()  # Return lowercase version for comparison

sorted_case_insensitive = sorted(fruits, key=ignore_case)  # Sort ignoring case
print("Using sorted() with key function (ignore case):", sorted_case_insensitive)

# Another example: Sort numbers based on their absolute value (though not necessary here)
sorted_numbers = sorted(numbers, key=lambda x: abs(x - 5))  # Sort by distance from 5
print("Using sorted() with lambda key (distance from 5):", sorted_numbers)

# 4. reduce() - From the functools module, reduces the list to a single value
# It applies a function cumulatively to the items.
from functools import reduce

def add(x, y):
    return x + y  # Function to add two numbers

reduced_result = reduce(add, numbers)  # Sum all numbers in the list
print("4. Using reduce() to sum numbers:", reduced_result)

# With lambda:
reduced_lambda_result = reduce(lambda x, y: x * y, numbers)  # Multiply all numbers
print("Using reduce() with lambda to multiply numbers:", reduced_lambda_result)

print("\nAll higher-order functions demonstrated!")
