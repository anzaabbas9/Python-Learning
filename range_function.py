"""total=0
for i in range(1,101):
    total+=i
print(total)"""

"""total=0
for i in range(0,101,2):
    total+=i
print(total)"""

#fizzbuzz job interview question
"""n=int(input("enter the number of values you want:"))
for i in range(0,n):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)"""

"""
Question 5 (range()) — Multiplication Table
Use range() in a for loop to print the multiplication table of a number (e.g., 5) from 1 to 10:"""
"""num=5
for i in range(1,11):
    print(f"{num} * {i} = {i*num}")"""

"""
New Question 6 (range() with negative step) — Countdown Using range()
Use range() with a negative step to print a countdown from 10 to 1 (without using a while loop 
this time — this is the same countdown from Question 1, but done using range() instead)."""
for i in range(10,0,-1):
    print(i)

