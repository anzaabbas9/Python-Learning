height=float(input("enter your height:"))
bill=0
if height>3:
    age=int(input("enter your age:"))
    if age<12:
        bill=50
        print("your ticket price is 50")
    elif age<=18:
        bill=250
        print("your ticket price is 250")
    else:
        bill=500
        print("your ticket price is 500")
    photo=input("are you wanna take photo?(y/n)")
    if photo == 'y'or photo=='Y':
        bill += 50
        print(f"your total bill is:{bill}")
else:
    print("dont ride")
print("thank you ! enjoy the ride")