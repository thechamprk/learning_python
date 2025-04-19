weight = int(input("Weight: "))

weight_type = input("(L)bs or (K)g: ")

if weight_type.upper() == 'L':
    kgs = weight * 0.45
    print(f"You are {kgs} kilograms.")
else:
    lbs = weight * 2.20
    print(f"You are {lbs} pounds.")