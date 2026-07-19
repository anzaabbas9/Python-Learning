"""total=0
for i in range(1,101):
    total+=i
print(total)"""

"""total=0
for i in range(0,101,2):
    total+=i
print(total)"""

#fizzbuzz job interview question
n=int(input("enter the number of values you want:"))
for i in range(0,n):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)