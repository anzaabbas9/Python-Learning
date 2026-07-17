"""
list is sequence of characters can be of same r diff types like mix list
reverse()->reverse a list
sort()->sort it
insert()->insert a element at specific element
remove()->remove an element
pop->remove a value n even return it
extend->add new element r list of element,min n max for min n max value 
access throught index as [],len()-> for length
"""
import random
names=input("enter names separated by comma:")
name_list=names.split(",")
"""length=len(name_list)
print(name_list)
random_choice=random.randint(0,length-1)
print(f"{name_list[random_choice]} will pay the bill")"""
person=random.choice(name_list)
print(f"{person} will pay the bill")



