import math
"""def info(height,width,cover):
    area=height*width
    cans=math.ceil(area/cover)
    print(f"{cans} are required for paint")
h=int(input("enter height of wall:"))
w=int(input("enter width of wall:"))
coverage=7
info(height=h,width=w,cover=coverage)"""
def num(n):
    isprime=True
    if n==1:
        isprime=False
    for i in range(2,math.ceil(n/2)+1):
        if n%i==0:
            isprime=False
        else:
            isprime=True
    if isprime:
        print("prime number")
    else:
        print("not a prime")
        
n=int(input("enter a value:"))
num(n)