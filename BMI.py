weight=int(input("enter your weight in kg:"))
height=float(input("enter your height in meters:"))
BMI=weight/height**2
if BMI<18.5:
    print(f"your BMI is:{round(BMI,2)} and you are underweight")
elif BMI<25 :
    print(f"your BMI is:{round(BMI,2)} and you are normal")
elif BMI<30:
   print(f"your BMI is:{round(BMI,2)} and you are overweight")
elif BMI<35:
    print(f"your BMI is:{round(BMI,2)} and you are obese")
else:
    print(f"your BMI is:{round(BMI,2)} and you are clinically obese")
