import random
print("==================================================================================")
print("             --------ROCK PAPER SCISSORS GAME---------")
print("==================================================================================")
choices=["rock","paper","scissors"]
user_choice=int(input("enter your choice(0->rock,1->paper,2->scissors):"))
if user_choice not in (0,1,2):
    print("invalid choice .you lose")
else:
    computer_choice=random.randint(0,2)
    print(f"you choose:{choices[user_choice]}")
    print(f"computer choose:{choices[computer_choice]}")
    if user_choice==computer_choice:
        print("its draw")
    elif user_choice == 2 and computer_choice == 0:
     print("computer win")
    elif user_choice == 0 and computer_choice == 2:
     print("you win")
    elif user_choice <computer_choice :
     print("you lose")
    elif user_choice > computer_choice :
        print("you win")
