#height squared divided by weight
height = float(input("What is your height in metres?"))
weight = float(input("What is your weight in kilograms?"))
squared_height = height * height
BMI = weight / squared_height
if BMI < 18.5:
    print("Your BMI is", BMI ". You are Underweight")
elif 18.5 <= BMI <= 24.9:
    print("Your BMI is", BMI ". You have a normal weight")
elif 25 <= BMI <= 29.9:
    print("Your BMI is", BMI ". You are overweight")
elif BMI > 30:
    print("Your BMI is", BMI ". You are Obese")

