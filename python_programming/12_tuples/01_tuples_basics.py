# A tuple is a Python data type used to create an ordered immutable collection of items 
# Tuples can contain a mixed set of data types like this: developer = ('Alice', 34, 'Developer')

# Tuples are similar to lists, but while lists are a mutable data type, tuples are immutable. 
# This means that the elements in a tuple cannot be changed once it's created.
programming_languages = ('Python', 'Java', 'C++', 'Rust')
# programming_languages[0] = 'JavaScript'  type error

# The tuple data type is an ordered sequence of elements that can be comprised of strings,
# numbers, or even other tuples. Tuples are immutable and use zero-based indexing, meaning
# that the first element of the tuple is at index zero.

names = ("Ahmad","zain","fayaz","ziad")
numbers = (6,2,5,4,9)
mix = ('zain',12,34.66,True)

print(names)   # ('Ahmad', 'zain', 'fayaz', 'ziad')
print(numbers) # (6, 2, 5, 4, 9)
print(mix)     # ('zain', 12, 34.66, True)
print()

print(names[0])  # Ahmad

# negative indexing in tuples
print(names[-1]) # ziad

# converting an iterable to tuple
my_name = 'zain ul islam'
print(tuple(my_name))  
# ('z', 'a', 'i', 'n', ' ', 'u', 'l', ' ', 'i', 's', 'l', 'a', 'm')

# Total number of elements in a tuple
print(len(names)) # 4

# updating an element of the tuple ❌ NOT ALLOWED
# names[0] = "Munir"  # TypeError

# deleting an element from the tuple ❌ NOT ALLOWED
# del mix[0]  # TypeError

# deleting the whole tuple ✔️ allowed
# del names
# print(names)  # NameError bcz there the names tuple is deleted

# Checking an element in a tuple
print('zain' in names) # True
print(99 in numbers)   # False

# Tuple inside a tuple
developer = ('Alice', 25, ('Python', 'Rust', 'C++'))
print(developer)        # ('Alice', 25, ('Python', 'Rust', 'C++'))
print(developer[2])     # ('Python', 'Rust', 'C++')
print(developer[2][0])  # Python



# slicing tuples (same as list)
desserts = ('cake', 'pie', 'cookies', 'ice cream')
print(desserts[1:3])  # ('pie', 'cookies')