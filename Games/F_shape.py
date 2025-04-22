"""
To print the shape
xxxxx
xx
xxxxx
xx
xx
"""

each_line = [5 ,2, 5, 2, 2]
for number_of_x in each_line:
    output = 'x' * number_of_x
    print(output)


#MOSH's Solution
"""
each_line = [5 ,2, 5, 2, 2]
for number_of_x in each_line: #this loop is to change the paragraph
    output = ''
    for count in range(number_of_x): #this loop is to assign number of x'es to a variable and then after exiting the loop we'll print that variable. for eg. that variable will contain 'x' * 5 = "xxxxx".
        output += 'x'
    print(output)
"""