print("Welcome to the Ultimate Fair Ride Calculator!")
ticket_price, photo_price = 0, 0


height = float(input("Enter your height(in Ft.): "))
if height < 3:
    print("You are too short to ride.")
else:
    #The price tag according to age.
    age = int(input("Enter your age: "))
    if age < 12:
        print("Your ticket price is Rs.150.")
        ticket_price = 150
    elif 12 < age < 18:
        print("Your ticket price is Rs.250.")
        ticket_price = 250
    else:
        print("Your ticket price is Rs.500.")
        ticket_price = 500

photos = input("Do you want to take photos(will cost Rs.50 more) ? (yes/no): ")
if photos.lower() == "yes":
    photo_price = 50

#Used sum function to make sure if I add multiple things like snacks in future then it would be easier to add'em all.
total = (ticket_price, photo_price)
grand_total = sum(total)

print(f"Your total fair = Rs.{grand_total}.")