has_high_income = True
has_good_credit = True

if has_high_income and has_high_income:
    print("Eligible for Loan!")

#we can use or operator also if you want to get atleast one condition to be true.

has_good_credit = True
has_criminal_record = True
if has_high_income and not has_criminal_record:
    print("Eligible for Loan!")
