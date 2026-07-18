"""
# Python Lists — Complete Notes
## What is a List?
A list is an **ordered, changeable (mutable)** sequence of elements.
Elements can be the same type or mixed types (int, float, str, bool, even other lists).
```python
movies = ["Inception", "Titanic", "Avatar", "Joker", "Matrix"]
mixed = [1, "hello", 3.14, True]
## Creating & Accessing
movies = ["Inception", "Titanic", "Avatar", "Joker", "Matrix"]
movies[0]        # first element -> "Inception"
movies[-1]       # last element -> "Matrix"{reverse or -ve  indexing also possible}
movies[1:3]      # slice -> ["Titanic", "Avatar"]
movies[::-1]     # reversed copy -> doesn't change original
len(movies)      # number of elements -> 5
## Adding Elements
| Method | What it does |
| `append(x)` | Adds `x` to the **end** of the list |
| `insert(i, x)` | Inserts `x` at index `i` (shifts others right) |
| `extend(list2)` | Adds all elements of `list2` to the end |
movies.append("Interstellar")        # add to end
movies.insert(2, "Parasite")         # insert at index 2
movies.extend(["Dune", "Oppenheimer"]) # add multiple
## Removing Elements
| `remove(x)` | Removes the **first occurrence** of value `x` |
| `pop(i)` | Removes element at index `i` and **returns it** (default: last item) |
| `clear()` | Empties the entire list |
movies.remove("Titanic")   # removes by value
last = movies.pop()        # removes & returns last item
first = movies.pop(0)      # removes & returns item at index 0
movies.clear()             # list becomes []
## Searching & Counting
movies.index("Avatar")   # returns index of first match
movies.count("Joker")    # counts occurrences of value
"Avatar" in movies        # True/False — membership check
## Sorting & Reversing
numbers = [5, 2, 8, 1]
numbers.sort()               # ascending, changes original list
numbers.sort(reverse=True)   # descending
numbers.reverse()            # reverses list in place
sorted(numbers)               # returns a NEW sorted list (original unchanged)
## Copying a List
copy1 = movies.copy()   # correct way to copy
copy2 = movies          # WRONG — this just points to the same list!
⚠️ If you do `copy2 = movies` (without `.copy()`), both variables point to the **same list in memory
**. Changing one changes the other.
## Min, Max, Sum (built-in functions, not list methods)
numbers = [5, 2, 8, 1]
min(numbers)   # smallest value
max(numbers)   # largest value
sum(numbers)   # total of all values
## Nested Lists (list inside a list)
matrix = [[1, 2], [3, 4]]
print(matrix[0])      # [1, 2]
print(matrix[0][1])   # 2
## Looping Through a List
for movie in movies:
    print(movie)
for i in range(len(movies)):
    print(i, movies[i])
## Mutability — Important Concept
Lists are **mutable**, meaning they can be changed in place without creating a new object.
This is why `.append()`, `.sort()`, `.reverse()`, etc. don't require reassignment — they directly
 modify the original list.
movies.append("Dune")   # modifies movies directly, no need for movies = movies.append(...)
Compare this to strings, which are **immutable** — any "change" actually creates a new string.
## Quick Reference Table
| Function/Method | Purpose |
| `append(x)` | Add to end |
| `insert(i, x)` | Add at index `i` |
| `extend(list2)` | Add multiple items |
| `remove(x)` | Remove by value |
| `pop(i)` | Remove by index, returns value |
| `clear()` | Empty the list |
| `sort()` | Sort ascending (in place) |
| `sort(reverse=True)` | Sort descending |
| `reverse()` | Reverse in place |
| `copy()` | Create a real copy |
| `index(x)` | Find index of value |
| `count(x)` | Count occurrences |
| `len()` | Number of elements |
| `min()`, `max()`, `sum()` | Built-in functions for numeric lists |
| `in` | Check membership |
"""
"""import random
names=input("enter names separated by comma:")
name_list=names.split(",")
length=len(name_list)
print(name_list)
random_choice=random.randint(0,length-1)
print(f"{name_list[random_choice]} will pay the bill")
#person=random.choice(name_list)
#print(f"{person} will pay the bill")"""
"""
1. Basic List Operations
Create a list of 5 of your favorite movies. Then:
Print the first and last movie
Add a new movie to the end
Remove one movie from the list
Print the final list and its length"""
"""
movies=input("enter your favourite 5 movies separated by comma:")
movies_list=movies.split(",")
print(f"first movie is{movies_list[0]} and last movie is {movies_list[4]}")
print(movies_list[0:2])
movies_list.append("inception")
print(movies_list)
last=movies_list.pop(4)
print(movies_list)
length=len(movies_list)
print(length)
"""








