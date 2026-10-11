kq = float(input("Enter your weight:"))
boy = float(input("Enter your height:"))
BMI = (kq) / (boy**2)
print(BMI)
if BMI < 18.5:
    print("Category: Underweight")
elif BMI > 18.5 and BMI < 24.9:
    print("Category: Normal Weight")
elif BMI > 25 and BMI < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")
