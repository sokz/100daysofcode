print("welcome to the tip calculator.")
tot_bill = float(input("What was the total bill? $"))
tip_perc = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

amount = (tot_bill*(1+(tip_perc/100)))/no_of_people

print(f"Each person should pay: ${amount:.2f}") # .2f rounds off the decimals