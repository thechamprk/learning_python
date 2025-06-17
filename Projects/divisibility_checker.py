print("Welcome to the Divisibility Checker!\nThis can only check integer values, float value could be checked after future updates.")

#INPUT ZONE
user_input = input("Please enter the number: ")
while user_input.isdigit() == False:
    print("Invalid input. Please enter a valid number.")
    user_input = input("Please enter the number: ")

#PROCESSING ZONE
number = user_input

length_of_number = len(number)


#For checking divisibility by 2
if(int(number[(length_of_number-1)])%2 == 0):
    print("The number is divisible by 2.")
#For checking divisibility by 3
if(sum(int(i) for i in number)%3 == 0):
    print("The number is divisible by 3.")