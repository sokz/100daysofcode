height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# determining the bmi 

bmi = weight/(height**2)

# Determining if the person is normal, underweight or overweight

if (bmi < 18.5):
    print(f"Your BMI is {bmi:.0f}, you are underweight.")
elif (bmi >= 18.5) and (bmi < 25):
    print(f"Your BMI is {bmi:.0f}, you have a normal weight.")
elif (bmi >= 25) and (bmi < 30):
    print(f"Your BMI is {bmi:.0f}, you are overweight.")
elif (bmi >= 30) and (bmi < 35):
    print(f"Your BMI is {bmi:.0f}, you are obese.")
else:
    print(f"Your BMI is {bmi:.0f}, you are clinically obese.")