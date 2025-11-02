kettle_boiled = True 

if kettle_boiled:
    print("Kettle done! Time to make chai!")


snack = input("What snack would you like? ").strip().lower()  
if snack == "cookies" or snack == "samosa":
    print(f"Order confirmed for {snack}!")
else:
    print(f"Sorry, {snack} is not available.")


prices = {
    "small": 10,
    "medium": 15,
    "large": 20
}

cup_size = input("Enter cup size (small, medium, large): ").strip().lower()
if cup_size in prices:
    print(f"Price for {cup_size} cup: {prices[cup_size]}")
else:
    print("Unknown cup size")


order_amount = float(input("Enter the order amount: "))

# Use ternary operator to decide delivery fee
delivery_fee = 0 if order_amount > 300 else 30


print(f"Order amount: {order_amount}")
print(f"Delivery fee: {delivery_fee}")
print(f"Total cost: {order_amount + delivery_fee}")



seat_type = input("Enter seat type (sleeper, AC, general, Luxury): ").strip().lower()
match seat_type:
    case "sleeper":
        print("Features: Sleeping berth, basic amenities, affordable for long journeys.")
    case "ac":
        print("Features: Air-conditioned compartment, comfortable seating, climate control.")
    case "general":
        print("Features: Basic seating, no additional amenities, budget-friendly.")
    case "luxury":
        print("Features: Premium service, meals included, entertainment options, spacious seating.")
    case _:
        print("Invalid seat type")

