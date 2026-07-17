name1=input("enter your name:")
name2=input("enter his/her name:")
str1=name1 + name2
new_str=str1.lower()
print(new_str)
t=new_str.count('t')
r=new_str.count('r')
u=new_str.count('u')
e=new_str.count('e')
true=t+r+u+e
l=new_str.count('l')
o=new_str.count('o')
v=new_str.count('v')
e=new_str.count('e')
love=l+o+v+e
score=str(true)+str(love)
score=int(score)
if score < 10 or score > 90:
    print(f"your score is:{score} and you go together like coke and mentus")
elif score >= 40 and  score <= 50:
    print(f"your score is:{score} and you are alright together")
else:
    print(f"your score is:{score} ")
 


