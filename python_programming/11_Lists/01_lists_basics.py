# The list data type is an ordered sequence of elements that can be comprised of strings,
#  numbers, or even other lists. Lists are mutable and use zero-based indexing, meaning 
# that the first element of the list is at index zero.

names = ["Ahmad","zain","fayaz","ziad"]
numbers = [6,2,5,4,9]
mix = ['zain',12,34.66,True]

print(names) # ['Ahmad', 'zain', 'fayaz', 'ziad']
print(numbers) # [6, 2, 5, 4, 9]
print(mix) # ['zain', 12, 34.66, True]
print()

print(names[0]) # Ahmad

# negative indexing in lists
print(names[-1]) # ziad

# converting an iterable to list
# An iterable is a special type of object that can be looped over one item at a time.
my_name = 'zain ul islam' # ['z', 'a', 'i', 'n', ' ', 'u', 'l', ' ', 'i', 's', 'l', 'a', 'm']
print(list(my_name))

# Total number of elements in a list
print(len(names)) # 4

# updating an element of the list
# accesing or updating an invalid index cause invalid index error
names[0] = "Munir"
print(names) # ['Ahmad', 'Munir', 'fayaz', 'ziad']
names[len(names) - 1] = "M H Khan"
print(names) # ['Munir', 'zain', 'fayaz', 'M H Khan']

# deleting an element from the list
del mix[0]
print(mix) # [12, 34.66, True]

# del names # delete the whole list
# print(names) # you will get name error bsz the names list is deleted

# Checking an element in a list
print('zain' in names) # True
print(99 in numbers) # False

# List inside a list
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(developer) # ['Alice', 25, ['Python', 'Rust', 'C++']]
print(developer[2]) # ['Python', 'Rust', 'C++']
print(developer[2][0]) # Python
