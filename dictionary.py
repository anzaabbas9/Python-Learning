"""
1. Build a Contact Card
Create a dictionary for a friend with keys: name, phone, email. Print each value individually, then 
update the phone number to a new value and print the whole dictionary again."""
"""contact = {
   "name":"anza",
   "phone_no":2345567,
   "e_mail":"anza@1234"
}
print(contact["name"])
print(contact["phone_no"])
print(contact["e_mail"])
contact["phone_no"]=34567
print(contact)"""

"""
2. Menu Price Lookup
Create a dictionary representing a menu, e.g. {"pizza": 800, "burger": 400, "pasta": 600}. Ask the 
user to type a food item, and print its price using .get() — if the item isn't on the menu,
 print "Item not available" instead of crashing."""
"""menu={
    "pizza": 800,
    "burger": 400,
    "pasta": 600
}
item=input("enter a food item:")
price=menu.get(item)
if price is None:
    print("item not avaliable")
else:
    print(price)"""

"""
Question 3 — Word Frequency Counter (manual version, no loop needed yet)
Create a dictionary to count how many times each letter appears in a word, e.g. "hello". """

"""letter_count={}
word=input("enter a word:")
letter_count['h'] = word.count('h')
letter_count['e'] = word.count('e')
letter_count['l'] = word.count('l')
letter_count['o'] = word.count('o')
print(letter_count)
for letter in word:
    letter_count[letter]=word.count(letter)
print(letter_count)"""

"""
Question 4 — Student Grade Book
Create a dictionary storing 3 students and their grades:"""
grades = {"Ali": 85, "Sara": 92, "Bilal": 78}
highest=max(grades.values())
if grades["Ali"]==highest:
    print("Ali",highest)
elif grades["Sara"]==highest:
    print("Sara",highest)
elif grades["Bilal"]==highest:
    print("Bilal",highest)
    