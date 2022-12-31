# Taking input of names
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

# Calculating "LOVE"
combined_names = name1 + name2
combined_names = combined_names.lower()
t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')
l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')

first_digit = t + r + u + e
second_digit = l + o + v + e

love = (first_digit*10) + second_digit

# Output Results

if (love < 10) or (love > 90):
    print(f'Your score is {love}, you go together like coke and mentos.')
elif (love >= 40) and (love <= 50):
    print(f'Your score is {love}, you are alright together.')
else:
    print(f'Your score is {love}.')

