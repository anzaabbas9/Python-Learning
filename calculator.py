def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

num1=int(input("enter 1st number:"))
while True:
    symbol=input("which operation do you want(+,-,*,/):")
    if symbol not in ['+','-','*','/']:
          print("invalid input")
          continue
    num2=int(input("enter 2nd number:"))
    if symbol=='+':
        result=add(num1,num2)
    elif symbol=='-':
            result=sub(num1,num2)
    elif symbol=='*':
            result=mul(num1,num2)
    elif symbol=='/':
                result=div(num1,num2)
    else:
         print("invalid input")
         continue
    print(f"{num1} {symbol} {num2} = {result}")
    choice=input("enter y to continue with previous value ,n for new value and x to exit:")
    if choice=='y':
          num1=result
    elif choice=='n':
          num1=int(input("enter 1st number:"))
    else:
          break
    
            