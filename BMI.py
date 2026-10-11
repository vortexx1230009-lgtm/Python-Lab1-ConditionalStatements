kq = float(input("Enter your weight:"))
boy = float(input("Enter your height:"))
BMI = (kq) / (boy**2)
print(BMI)
if BMI < 18.5:
    print("You are underweight, thin")
elif BMI > 18.5 and BMI < 25:
    print("you are weight is normal")
elif BMI > 25 and BMI < 30:
    print("you are overweight")
else:
    print("You are obese, obesity")
