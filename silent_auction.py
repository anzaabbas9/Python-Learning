import os
print("***********WELCOME TO SILENT AUCTION***********")
auc={}
while True:
    name=input("enter your name:")
    bid_price=int(input("enter your bid price:"))
    auc[name]=bid_price
    isperson=input("is there any other person(yes/no)")
    if isperson.lower()=='no':
        break
    os.system('cls' if os.name == 'nt' else 'clear')    
highest=max(auc.values())
for person in auc:
    if auc[person]==highest:
        print(f"{person} win with a bid of {highest}")