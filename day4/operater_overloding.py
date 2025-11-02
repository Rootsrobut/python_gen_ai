base_liquid=['water','milk']
extra_flavor=['ginger']

full_liquid_mix=base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

strong_brew=['black tea','water']*3
print(f'String brew : {strong_brew}')

# Create an empty bytearray of a specific size
my_bytearray = bytearray(5) 
print(my_bytearray) 

# Create a bytearray from an iterable of integers (0-255)
my_bytearray_from_list = bytearray([72, 101, 108, 108, 111]) 
print(my_bytearray_from_list) 

# Create a bytearray from a string with a specified encoding
my_bytearray_from_string = bytearray("Hello", "utf-8")
print(my_bytearray_from_string) 

# Modify an individual byte
my_bytearray_from_string[0] = 87 # Change 'H' to 'W' (ASCII 87)
print(my_bytearray_from_string)

# Append a byte
my_bytearray_from_string.append(33) # Append '!' (ASCII 33)
print(my_bytearray_from_string)

# Extend with another byte sequence
another_byte_sequence = bytearray([32, 87, 111, 114, 108, 100]) # " World"
my_bytearray_from_string.extend(another_byte_sequence)
print(my_bytearray_from_string)

raw_spice_data=bytearray(b"CINNAMON")
raw_spice_data=raw_spice_data.replace(b'CINNA',b'CARD')
print(f"Bytes:{raw_spice_data}")