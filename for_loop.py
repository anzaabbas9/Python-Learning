"""heights=input("enter the heights separated by comma(,):")
new_height=heights.split(",")
print(new_height)
count=0
for i in new_height:
    count+=1
print(f"length->{count}")
for i in range(count):
    new_height[i]=int(new_height[i])
print(new_height)
total=0
for j in new_height:
    total+=j
avg=total/count
print(f"average is:{round(avg)}")"""

"""list1=input("enter numbers separated by space:")
new_list=list1.split()
count=0
for i in new_list:
    count+=1
for i in range(count):
    new_list[i]=int(new_list[i])
max=new_list[0]
print(new_list)
for i in new_list:
    if i> max:
        max=i
print(f"max value:{max}")"""

n=[1,2,3,4,5]
squared=[]
for i in n:
    i=i**2
    squared.append(i)
print(squared)
