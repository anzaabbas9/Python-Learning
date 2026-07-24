"""
A set is an unordered collection of unique elements — no duplicates allowed, and no indexing (since there's no order).

pythonfruits = {"apple", "banana", "cherry"}

⚠️ Sets don't preserve order and can't be accessed with fruits[0] — that will raise a TypeError.

Removing Duplicates (common use case)

pythonnumbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))   # removes duplicates, converts back to list

Adding & Removing Elements

pythonfruits.add("mango")        # add one item
fruits.remove("banana")    # remove item (error if not found)
fruits.discard("kiwi")     # remove item (NO error if not found)
fruits.pop()                # removes a random item (sets have no order)
fruits.clear()               # empties the set

Set Operations — Return a NEW Set (original unchanged)

MethodWhat it doesunion(other)All elements from both sets, no duplicatesintersection(other)Elements common to both setsdifference(other)Elements in this set but NOT in the othersymmetric_difference(other)Elements in either set, but NOT in both

pythona = {"Ali", "Sara", "Bilal", "Zain"}
b = {"Sara", "Zain", "Hina", "Omar"}

a.union(b)                  # {Ali, Sara, Bilal, Zain, Hina, Omar}
a.intersection(b)           # {Sara, Zain}
a.difference(b)              # {Ali, Bilal}
a.symmetric_difference(b)    # {Ali, Bilal, Hina, Omar}

The _update Versions — Modify the Original Set IN PLACE (return None)

MethodWhat it doesupdate(other)Merges other into the set directlyintersection_update(other)Keeps only common elements, in placedifference_update(other)Removes elements found in other, in placesymmetric_difference_update(other)Keeps only non-common elements, in place

pythona.update(b)   # a is now changed directly — this returns None, so don't print the return value!
print(a)      # print `a` itself to see the result

⚠️ Common mistake: print(a.update(b)) prints None, since update() doesn't return the set — it just modifies a and returns nothing. Always print the set on its own line afterward.

⚠️ Chaining warning: if you call multiple _update methods back-to-back on the same set, each one operates on the already-modified result of the previous one — not the original. Use .copy() if you want to test each operation independently:

pythona1 = a.copy()
a1.update(b)

a2 = a.copy()
a2.difference_update(b)

The Pattern to Remember (same idea as lists: .sort() vs sorted())

Without _updateWith _updateReturns a new setChanges the original setOriginal stays unchangedOriginal is modified in place

Membership Check

python"Sara" in a   # True/False

Converting Between List and Set

pythonset(my_list)     # list -> set (removes duplicates, loses order)
list(my_set)      # set -> list (gains indexing back)"""

"""set1={1,6,5.6,'anza'}
set2={3,8,6,9.8}
print(set1.difference_update( set2))
print(set1.union( set2))
print(set1.intersection_update( set2))
print(type(set1))
print(len(set1))"""
"""
Create two sets of friend names for two different people. Use set operations to find:

Friends they have in common (intersection)
Friends only person A has (difference)
All friends combined, no duplicates (union)"""
person_a = {"Ali", "Sara", "Bilal", "Zain"}
person_b = {"Sara", "Zain", "Hina", "Omar"}
# find intersection, difference, and union
#person_a.update(person_b)
#print(person_a)
#person_a.intersection_update(person_b)
person_a.difference_update(person_b)
print(person_a)
#person_a.symmetric_difference_update(person_b)
#print(person_a)