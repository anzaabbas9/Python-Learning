import random
import art_log
EASY_ATTEMPTS=10
DIFFICULT_ATTEMPTS=5
def difficulty(level):
    if level=="easy":
        return EASY_ATTEMPTS
    elif level=="difficult":
        return DIFFICULT_ATTEMPTS
    else:
        return None
    
def check_num(guess,num,attempts):
    if guessed_num>num:
        print("your guess is too high")
        return attempts-1
    elif guessed_num<num:
        print("your guess is to low")
        return attempts-1
    else:
        return attempts
        
print(art_log.logo)
print("lemme think a number between 1 and 50")
num=random.randint(1,50)
level=input("choose level of difficulty ...easy or difficult..")
attempts=difficulty(level)
if attempts is None:
    print("invalid input, exiting")
else:
    guessed_number = 0
while guessed_number!=num:
    print(f"you have {attempts} remaining to guess number")
    guessed_num=int(input("guesss a number:"))
    attempts=check_num(guessed_num,num,attempts)
    if guessed_num==num:
        print(f"your guess is correct {guessed_num} .....you win")
        break
    if attempts==0:
            print("you are out of attempts ...you lose")
            break
