
# Hashing in Data Structures
students = {"Alice": 25, "Bob": 30}
print(students["Bob"])  


# Built-in hash() Function
print(hash("hello"))      # e.g., 123456789 (value varies)
print(hash(123))          # hash of an integer
print(hash((1, 2, 3)))    # hash of a tuple

# Cryptographic Hashing (for security)

import hashlib 

text = "hello world"
hash_object = hashlib.sha256(text.encode())
print(hash_object.hexdigest())  # SHA-256 hash



class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __hash__(self):
        return hash((self.name, self.id))  # combine attributes

    def __eq__(self, other):
        return (self.name, self.id) == (other.name, other.id)

s1 = Student("Alice", 1)
s2 = Student("Alice", 1)

print(hash(s1), hash(s2))  # same hash
print(s1 == s2)            # True

