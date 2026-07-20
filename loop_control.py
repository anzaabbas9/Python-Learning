"""
Question 3 (Control Statement — break) — Find First Even Number
Loop through the list numbers = [3, 7, 9, 4, 11, 6] and use break to stop as soon as you find the 
first even number. Print that number."""
"""number=[1,7,9,3,5,6,8,4]
count=0
while count<len(number):
    if(number[count]%2==0):
        print(f"first even number:{number[count]}")
        break
    count+=1"""

"""
Question 4 (Control Statement — continue) — Skip Negatives
Loop through values = [4, -2, 7, -5, 9, -1] and use continue to skip negative numbers,
 printing only the positive ones."""
values=[4,-2,6,80,-1]
for i in values:
    if(i<0):
        continue
    print(i)