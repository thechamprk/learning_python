current_age = int(input("How old are you? "))
remaining_years = 90 - current_age

remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 54
remaining_days = remaining_years * 365

print(f"Before reaching 90, you have:\n{remaining_years} years,\n{remaining_months} months,\n{remaining_weeks} weeks,\n{remaining_days} days.")