def process_order(item, quantity):
    try:
        if not isinstance(quantity, (int, float)):
            raise TypeError("Quantity is not a number")
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry, that chai is not on menu")
    except TypeError as e:
        print(f"Error:{e}")


process_order("ginger", 1)
process_order("masala", "two")
process_order("masala", 3)