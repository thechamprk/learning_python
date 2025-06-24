print("\nWelcome to BluePizza.co - The Best Pizza in Town!\nHow we can serve you today?")
order = input("We have the following sizes available:\nS: Small Pizza @ Rs.100\nM: Medium Pizza @ Rs.200\nL: Large Pizza @ Rs.300\nQ: Quit\n")

bill = 0
if order == "S":
    bill = 100
elif order == "M":
    bill = 200
elif order == "L":
    bill = 300
elif order == "Q":
    print("Thank you for visiting BluePizza.co!")
    exit()
else:
    print("Invalid Input.")
    exit()

pepperoni = input("Do you want pepperoni \n@ Rs.30 for Small Pizza\n@ Rs.50 for Medium or Large Pizza? (Y/N): ")

if pepperoni == "Y":
    if order == "S":
        bill += 30
    else:
        bill += 50

extra_cheese = input("Do you want extra cheese @just Rs.20? (Y/N)")
if extra_cheese == "Y":
    bill += 20

print(f"\nYour Net-Payable amount: Rs.{bill}\nThank you for visiting BluePizza.co!")