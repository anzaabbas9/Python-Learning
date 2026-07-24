"""
1. Countdown Timer
Write a while loop that counts down from 10 to 1, printing 
each number, then prints "Liftoff!" at the end."""
"""count=10
while count>=1:
    print(count)
    count-=1
print("liftoff")"""

"""
New Question 1 (While Loop) — Guess the Number (Simplified)
Set a secret number, e.g. secret = 7. Use a while loop to keep asking the user to guess the number
 with input(). Keep looping until they guess correctly then print "You got it!"."""
"""secret=7
guess=int(input("guess a number:"))
while guess!=secret:
    guess=int(input("guess a number:"))
print("you got it!")"""

"""
New Question 2 (While Loop) — Password Attempts
Set a correct password, e.g. password = "python123". Give the user up to 3 attempts to enter it 
correctly using a while loop. If they get it right, print "Access granted". 
If they run out of attempts, print "Access denied"."""
password='python123'
attempt=0
while attempt<3:
        user_attempt=input("enter a password(remember you have 3 attempts only):")
        if(user_attempt==password):
            print('"access guranted"')
            break
        attempt+=1
else:
    print('"access denied"')

