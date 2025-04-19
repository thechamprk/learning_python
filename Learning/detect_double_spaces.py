"""
Write a program to detect double spaces in a string and
We have to replace the double spaces with single spaces.
"""

place = input("I want to live in a dreamy place where it should be? ")
double_space = "  " in place

if double_space == 1:
    print("You've entered a double space")
    corrected_place = place.replace("  ", " ")
    print(f"'{corrected_place}' is a great choice for for living!")
else:
    print(f"'{place}' is a great choice for for living!")


