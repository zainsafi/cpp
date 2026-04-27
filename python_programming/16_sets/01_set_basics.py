# SETS IN PYTHON
# A set is an unordered and mutable collection of UNIQUE elements.
# It automatically removes duplicate values and does not support indexing.

set_A = {1, 2, 3, 4, 5}
print(set_A)


# EMPTY SET
# {} creates an empty dictionary, NOT a set
# To create an empty set, we must use set()

empty_set = set()
print(empty_set)

empty_dict = {}
print(type(empty_dict))  # <class 'dict'>


# ADD ELEMENT
# add() is used to insert a new element into the set

set_A.add(6)
print(set_A)

# If the element already exists, it will NOT be added again
# because sets only store unique values

set_A.add(5)
print(set_A)


# REMOVE ELEMENT
# remove() deletes the element but raises an error if not found

set_A.remove(4)
print(set_A)

# discard() also deletes the element but DOES NOT raise error if not found

set_A.discard(10)
print(set_A)


# CLEAR SET
# clear() removes ALL elements from the set

temp_set = {1, 2, 3}
temp_set.clear()
print(temp_set)  # set()


# SET OPERATIONS
# Sets support mathematical operations similar to real math sets

set_A = {1, 2, 3, 4, 5}
set_B = {2, 3, 4, 6}


# issubset(): checks if all elements of one set are inside another set

print(set_B.issubset(set_A))   # False

# issuperset(): checks if a set contains all elements of another set

print(set_A.issuperset(set_B)) # False


# isdisjoint(): checks if two sets have NO common elements

print(set_A.isdisjoint(set_B)) # False


# union (|): combines all elements from both sets (no duplicates)

print(set_A | set_B)  # {1, 2, 3, 4, 5, 6}


# intersection (&): returns only common elements

print(set_A & set_B)  # {2, 3, 4}


# difference (-): elements present in first set but not in second

print(set_A - set_B)  # {1, 5}


# symmetric difference (^): elements in either set but NOT both
# A ^ B = (A - B) U (B - A)

print(set_A ^ set_B)  # {1, 5, 6}


# COMPOUND OPERATORS |= &= -= ^=
# These operators update the original set directly

set_A = {1, 2, 3, 4, 5}
set_B = {2, 3, 4, 6}

# -= removes common elements from set_A
set_A -= set_B
print(set_A)  # {1, 5}

# similar can done be done for other operations

# MEMBERSHIP CHECK
# 'in' keyword is used to check if an element exists in the set

print(5 in set_A)   # True
print(10 in set_A)  # False

