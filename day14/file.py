print("--- Writing Masala Chai order (Method 1: try/finally) ---")
file = open("order.txt", "w")
try:
    file.write("Masala chai - 2 cups\n")
    print("Content written successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    file.close()
    print("File closed manually.")
print("\n--- Writing Ginger Tea order (Method 2: with statement) ---")
try:
    with open("order.txt", "a") as file:  # Using 'a' (append) to add to existing file
        file.write("Ginger tea - 4 cups\n")
        print("Content appended successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

    
print("File closed automatically by 'with' statement.")
print("\n--- Reading Final order.txt Content ---")
with open("order.txt", "r") as file:
    print(file.read())
