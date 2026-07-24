import random
import game_art
import game_database
import os
print(game_art.logo)
def display(candidate):
    name=candidate["name"]
    country=candidate["country"]
    description=candidate["description"]
    return f" {name} a {description},,from {country},"


def check_guess(guess,f1,f2):
    if f1>f2:
        if guess==1:
            return True
        else:
            return False
    else:
        if guess==2:
            return True
        else:
            return False

        
candidate2=random.choice(game_database.data)
ischeck=True
score=0
while ischeck:
    candidate1=candidate2
    candidate2=random.choice(game_database.data)
    while candidate1==candidate2:
         candidate2=random.choice(game_database.data)
    print(f"compare 1: {display(candidate1)}")
    print(game_art.vs)
    print(f"compare 2:{display(candidate2)}")
    guess=int(input("which one has more followers..... type 1 or 2:"))
    follower1=candidate1["follower"]
    follower2=candidate2["follower"]
    iscorrect=check_guess(guess,follower1,follower2)
    os.system('cls')
    print(game_art.logo)

    if iscorrect:
        score+=1
        print(f"your guess is correct.. and your score is {score}")
    else:
        print(f"your guess is incorrect and your final score is {score} ")
        ischeck=False