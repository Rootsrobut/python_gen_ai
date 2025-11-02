value=13
remainder=value%5
if remainder:
    print(f"Not divisible,remainder is {remainder}")

value=13
if remainder:=value%5:
    print(f"Not divisible,remainder is {remainder}")

# available_sizes = ["small", "medium", "large"]
# if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
#     print(f"Serving {requested_size} chai")    


flavors = ["masala", "ginger", "lemon", "mint"]
print("Available flavors: ", flavors)
while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available. Please try again.")
print(f"You chose {flavor} chai. Enjoy! ☕")    