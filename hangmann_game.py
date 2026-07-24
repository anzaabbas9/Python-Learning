import random

word_list = ["apple", "tiger", "eagle", "carrot", "ali"]
stages = [
    """
-+----+
  |   |
  O   |
 /|\\ |
 / \\ |
      |
=========
""",
    """
-+----+
  |   |
  O   |
 /|\\ |
 /    |
      |
=========
""",
    """
-+----+
  |   |
  O   |
 /|\\ |
      |
      |
=========
""",
    """
-+----+
  |   |
  O   |
  |\\ |
      |
      |
=========
""",
    """
-+----+
  |   |
  O   |
  |   |
      |
      |
========
""",
    """
-+----+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
-+----+
  |   |
      |
      |
      |
      |
=========
""",
]
word = random.choice(word_list)
attempt = 6
print(list(word))
blank_list = ["-"] * len(word)
print(blank_list)
print(" ".join(blank_list))
while True:
    letter = input("guess a letter:")
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                blank_list[i] = letter
    else:
        attempt -= 1
    print(" ".join(blank_list))
    print(stages[attempt])
    if "-" not in blank_list:
        break
    if attempt <= 0:
        break
if "-" not in blank_list and attempt > 0:
    print("you win!")
else:
    print("you lose!")
