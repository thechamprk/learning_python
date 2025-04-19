"""
Price os a house is $1M
If a buyer has good credit,
    they need to put down 10%
Otherwise
    they need to put down 20%
Print the down payment.
"""

#Solution
credit_score = int(input("What's your Credit Score?\n"))
House_Price = 1000000

if credit_score > 650:
    down_payment = House_Price * 0.1
else:
    down_payment = House_Price * 0.2
print(f"Down Payment: {down_payment}")

#Mosh's Solution
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")