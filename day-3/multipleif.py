# Nested if-else construct
print("Welcome to the rollercoaster!")

# Input Height
height = int(input("What is your height in cm? "))

# Nested if-else construct for checking the height requirement and determining the ticket rate acc. to the age of the user
if (height > 120):
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    # Bill generation acc to age
    if(age <= 18):
        bill = 7
        print(f"Youth tickets are ${bill}")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}")
    choice = input("Do you want photos? (y/n)")
# Asking for choice of photos
    if(choice =="y"):
        bill += 3
        print(f"Total bill is {bill}")
    else:
        print(f"Total bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride the rollercoaster.")
