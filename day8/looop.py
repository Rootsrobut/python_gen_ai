seats = ["booked", "booked", "available"]
for seat in seats:
    if seat == "available":
        print("Available seat found!")
        break
    else:
       print("All seats are booked.") 



menu = ["Green", "Lemon", "Spiced", "Mint"]
for idx, item in enumerate(menu, start=1):
    output_line = f"({idx}) : {item} chai"
    print(output_line)



names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [150, 70, 100, 55]


for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")





seats = ["sleeper", "AC", "general", "luxury", "sleeper"]
availability = [True, False, True, True, False] 
prices = [500, 1000, 200, 1500, 500] 
booking_successful = False
attempts = 0
max_attempts = 3

while attempts < max_attempts and not booking_successful: 
    print(f"\nAttempt {attempts + 1}/{max_attempts}")
    print("Available seats:")
    for index, (seat, avail, price) in enumerate(zip(seats, availability, prices), start=1): 
        if avail: 
            continue
        print(f"{index}. {seat.capitalize()} - Price: {price}")
    selected_index = None
    for _ in range(5): 
        try:
            selected_index = int(input("Select seat number (1-5): ")) - 1
            if 0 <= selected_index < len(seats):
                break 
            else:
                print("Invalid or unavailable seat. Try again.")
                continue  
        except ValueError:
            print("Please enter a number.")
            continue
    else: 
        print("Too many invalid attempts. Skipping booking.")
        attempts += 1
        continue
    selected_seat = seats[selected_index]
    selected_price = prices[selected_index]
    confirm = input(f"Confirm booking for {selected_seat} at {selected_price}? (yes/no): ").strip().lower()
    if confirm == "yes":
        print(f"Booking successful for {selected_seat}!")
        booking_successful = True
        availability[selected_index] = False 
    else:
        print("Booking cancelled.")
        attempts += 1

if booking_successful:
    print("\nThank you for booking!")
else:
    print("\nBooking failed after max attempts.")
