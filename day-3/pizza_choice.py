# Input choices
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L :")
add_pepperoni = input("Do you want pepperoni? Y or N :")
extra_cheese = input("Do you want extra cheese? Y or N :")

# Logic for calculating the bill

# Small Pizza : $15
# Medium Pizza : $20
# Large Pizza  : $25
# Pepperoni for small pizza: +$2
# Pepperoni for medium or large pizza: +$3

# Extra cheese for any size : +$1
if(size == "S"):
    bill = 15
elif(size == "M"):
    bill = 20
else:
    bill = 25

if(add_pepperoni == "Y"):
    if(size == "S"):
        bill += 2
    else:
        bill += 3

if(extra_cheese == "Y"):
    bill += 1

print(f"Your final bill is ${bill}")
