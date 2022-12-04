# Asking for input to check if odd or even
number = int(input("Which number do you want to check? "))

# if-else construct to give out appropriate output 
if (number%2 == 0):
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")