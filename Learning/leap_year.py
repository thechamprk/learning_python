user_input =  int(input("Enter the year: "))

if (user_input%4 == 0 and (user_input % 100 != 0 or user_input%400 == 0)):
    print("The given year is a leap year.")
else:
    print("The given year is not a leap year.")