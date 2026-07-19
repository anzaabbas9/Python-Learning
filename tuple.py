"""
TUPLES
A tuple is an ordered, immutable (unchangeable) sequence of elements.
Once created, you cannot add, remove, or modify its elements.
pythonstudent = ("Ali", 20, "A")
single = ("apple",)   # note the comma — needed for a single-item tuple!

Accessing Elements (same as lists)

pythonstudent[0]        # "Ali"
student[-1]       # "A" (last item)
student[0:2]       # ("Ali", 20) — slicing
len(student)       # 3

Only 2 Built-in Methods

Since tuples can't be modified, they only have 2 methods:

MethodWhat it doescount(x)Counts occurrences of value xindex(x)Returns index of first occurrence of x

pythonstudent.count("A")     # 1
student.index(20)      # 1

Immutability — The Key Concept

pythonstudent[1] = 21

This raises:

TypeError: 'tuple' object does not support item assignment

You cannot reassign, append, or remove elements from a tuple.

Why Use a Tuple Instead of a List?


Data that shouldn't change (coordinates, RGB colors, days of the week)
Slightly faster, uses less memory than lists
Can be used as dictionary keys (lists cannot, since they're mutable)


Converting Between List and Tuple

pythonlist(my_tuple)     # tuple -> list (now editable)
tuple(my_list)      # list -> tuple (now locked)"""

"""tuple1=(1,5,60,35,-34)
print(tuple1[-2])
print(tuple1.count(5))
tuple2=(7,)
print(list(tuple1))
print(type(tuple2))
tuple3=(tuple1,tuple2)
print(tuple3)"""
"""
Create a tuple storing a student's info: (name, age, grade). Print each value individually using 
indexing, then try to change the age and observe what error Python gives you."""
"""student=("ali",21,'B')
print(student[0:3])
student[1]=34
print(student[0:3])"""

"""
Create two tuples representing points: point1 = (2, 3) and point2 = (5, 7). 
Access the x and y values from each tuple and print them separately."""
p1=(2,3)
p2=(5,7)
x1=p1[0]
y1=p1[1]
x2=p2[0]
y2=p2[1]
print(f"x1->{x1} and y1->{y1}")
print(f"x2->{x2} and y2->{y2}")

