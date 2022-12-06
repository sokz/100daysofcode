# Input for the year 
year = int(input("Which year do you want to check? "))

# Logic for determining leap year

if (year%4 == 0):
    # Placeholder
    if (year%100 == 0):
        if (year % 400 == 0):
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")

        
