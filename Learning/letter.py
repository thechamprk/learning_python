"""
Write a program to fill in a letter template given below
with name and date.
        letter = ''' Dear <|NAME|>,
                            you are selected!
                            <|DATE|> '''
"""
from datetime import date #got this module from web coz I want to print the latest provided date.
NAME = "Rounak"
DATE = date.today()

print(f"Dear {NAME},\n\t\tyou are selected!\n\t\t{DATE}")