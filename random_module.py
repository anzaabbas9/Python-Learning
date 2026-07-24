import random
"""to use this module first write import module on front of prog n must add module before use
random.randint(a,b) ->for int range a>=x<=b
random.randrange(a,b) -> also for int but range is a>x<=b
random.random()-> for float bydefault range is 0.000 to 1
random.uniform() -> to given your own range for float
random.shuffle()->to shuffle a list as l=[1,2,3,4] to any sequence
random.choice()->to pick a random number from list"""
print("-----virtual coin toss program-----")
toss=random.randint(0,1)
if toss==1:
    print("tail")
else:
    print("head")