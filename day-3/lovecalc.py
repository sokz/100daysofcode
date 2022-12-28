# Taking input of names
print("Welcome to the Love Calculator!")
first_name = input("What is your name? \n").lower()
second_name = input("What is their name? \n").lower()

# Calculating "LOVE"

count_t = first_name.count("t") + second_name.count("t")
count_r = first_name.count("r") + second_name.count("r")
count_u = first_name.count("u") + second_name.count("u")
count_e = first_name.count("e") + second_name.count("e")

first_digit = count_t + count_r + count_u + count_e

count_l = first_name.count("l") + second_name.count("l")
count_o = first_name.count("o") + second_name.count("o")
count_v = first_name.count("v") + second_name.count("v")

second_digit = count_l + count_o + count_v + count_e

love = (first_digit*10) + second_digit

# Output Results

if (love < 10) or (love > 90):
    print(f'Your score is {love}, you go together like coke and mentos.')
elif (love >= 40) and (love <= 50):
    print(f'Your score is {love}, you are alright together.')
else:
    print(f'Your score is {love}')

