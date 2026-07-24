print("-------online pizza order system--------")
small=100
medium=200
large=300
bill=0
size=input("which size of pizza you want:")
if size=='small':
    bill=100
    print("small size price  is 100")
    pep=input("do you wanna peproni(y/n)")
    if pep=='y'or pep=='Y':
        bill+=30
        print("your bill  current is 100 and peproni for small pizza is 30")
    else:
         print(f"your bill is {bill}")
elif size=='medium':
    bill=200
    print("medium size price is 200")
    pep=input("do you wanna peproni(y/n)")
    if pep=='Y' or pep=='y':
        bill+=50
        print("your bill current  is 200 and peproni for medium pizza is 50")
    else:
         print(f"your current bill is {bill}")
else:
    bill=300
    print("large size price  is 300")
    pep=input("do you wanna peproni(y/n)")
    if pep=='y' or pep=='Y':
         bill+=50
         print("your bill current  is 300 and peproni for large pizza is 50")
    else:
         print(f"your current bill is {bill}")

cheese=input("do you want extra cheese(y/n)")
if cheese=='y'or cheese=='Y':
    bill+=50
    print(f"your total bill is: {bill}")
else:
    print(f"your total bill is:{bill}")


   

