
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))


bmi = int (weight / height ** 2)  #calculate BMI 


if bmi <= 18:
    print(f"your bmi is{bmi},You have underweight.")
elif 18 < bmi <= 25:
        print(f"your bmi is {bmi},You have normal weight.")
elif 25 < bmi <=30:
        print(f"your bmi is {bmi}You have overweight.")
elif 30 < bmi <=35:
        print(f"your bmi is {bmi}You have obese.")
else:print("You have are clinically obese.")

