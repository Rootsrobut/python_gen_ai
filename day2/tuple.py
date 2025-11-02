empty_tuple = ()
print(empty_tuple)  
my_tuple = (1, 2, 3, 'apple', 4.5)
print(my_tuple) 
another_tuple = tuple([1, 2, 3])  
print(another_tuple) 
single_element = (5,) 
print(single_element)  



my_tuple = (1, 2, 3, 'apple')
print(my_tuple[0]) 
print(my_tuple[3]) 
print(my_tuple[-1]) 
print(my_tuple[1:3]) 
print(my_tuple[:2])  
print(my_tuple[2:]) 
print(len(my_tuple)) 


tuple1 = (1, 2)
tuple2 = (3, 4)
new_tuple = tuple1 + tuple2 
print(new_tuple) 

repeated_tuple = my_tuple * 3
print(repeated_tuple)
print(2 in my_tuple)   
print(4 not in my_tuple)  
for item in my_tuple:
    print(item)

print(my_tuple.count(2))
print(my_tuple.index(2))  # Output: 1 (first occurrence at index 1)


my_tuple = (1, 2, 3)
a, b, c = my_tuple  # Unpacking
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Extended unpacking
first, *rest = my_tuple
print(first)  # Output: 1
print(rest)   # Output: [2, 3] (rest is a list)


nested_tuple = (1, (2, 3), (4, 5))
print(nested_tuple[1])  # Output: (2, 3)
print(nested_tuple[1][0])  # Output: 2



my_tuple = (1, 2, 3)
my_tuple[0] = 10  # Error: 'tuple' object does not support item assignment
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]
my_set = set(my_tuple)
print(my_set)  # Output: {1, 2, 3} (removes duplicates)
back_to_tuple = tuple(my_list)
print(back_to_tuple)  # Output: (1, 2, 3)