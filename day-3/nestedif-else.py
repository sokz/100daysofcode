# Nested if-else construct
print("Welcome to the rollercoaster!")

# Input Height
height = int(input("What is your height in cm? "))

# Nested if-else construct for checking the height requirement and determining the ticket rate acc. to the age of the user
if (height > 120):
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if (age < 12):
        print("Child tickets are $5")
    elif (age <= 18):
        print("Youth tickets are $7")
    elif(age >= 45) and (age <= 55):
        print("Everything is going to be okay. Have a ride on us!")
    else:
        print("Adult tickets are $12")
else:
    print("Sorry, you have to grow taller before you can ride the rollercoaster.")
