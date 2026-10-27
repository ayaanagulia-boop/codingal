print("------BMI calculator------\n\n\n")
w= int(input("Enter your weight in kilograms: "))
h= int(input("Enter your height in centimeters: "))

bmi= w/((h/100)**2)
"""
18.4
24.9
29.9
34.9
39.9

"""
if bmi <= 18.4:
    print("Catagory- underweight")
elif bmi <= 24.9:
    print("catagory- Normal range")
elif bmi<=29.9:
    print("Catagory- overweight")
elif bmi<= 34.9:
    print("Catagory- severly overweight")
elif bmi<= 39.9:
    print("Catagory- obese")
else:
    print("Catagory- severly obese")