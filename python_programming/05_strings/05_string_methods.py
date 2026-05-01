# some common string methods

import re

my_name_1 = "zain Ul Islam"
my_name_2 = " zain Ul Islam "

print(my_name_1.upper()) # string to upper case
print(my_name_1.lower()) # string to lower case
print(my_name_1.isupper()) # False
print(my_name_1.islower()) # False
print(my_name_1.lower().islower()) # True
print(my_name_1.capitalize()) # capatilize the first character only
# title(): Returns a new string with the first letter of each word capitalized.
print("hi i am title".title())

# strip(): Returns a new string with the specified leading and trailing characters removed.
# If no argument is passed it removes leading and trailing whitespace.
print(my_name_2.strip()) # zain Ul Islam
print(my_name_2.strip(" zain")) # Ul Islam

# replace(old, new): Returns a new string with all occurrences of old replaced by new.
print(my_name_1.replace("zain","Zia")) # Zia Ul Islam

# split(separator): Splits a string on a specified separator into a list of strings.
# If no separator is specified, it splits on whitespace.
# handles multiple spaces, tabs, newlines
print(my_name_1.split()) # ['zain', 'Ul', 'Islam']
# splits only on single spaces
print(my_name_1.split(" ")) # ['zain', 'Ul', 'Islam']
# .rsplit() (split from the right)
print("one two three".rsplit(' ',1)) # ['one two', 'three']

# .partition() (splits into 3 parts)
# structure = (before, separator, after)
print("Zain Ul Islam".partition(" ")) # ('Zain', ' ', 'Ul Islam')
# .rpartition() (from the right)
print("Zain Ul Islam".rpartition(' ')) # ('Zain Ul', ' ', 'Islam')

# Using re.split() (advanced, powerful)
my_name_3 = "Zain.Ul;Islam"
print(re.split('[.;]',my_name_3)) # ['Zain', 'Ul', 'Islam']

# join() is used to combine (join) elements of a list (or any iterable) into a single string.
# Syntax: separator.join(iterable) separator → what you want between elements
words = ["Hello","World!","How","are","you"]
print(' '.join(words)) # Hello World! How are you
print('-'.join(['2026', '02', '15'])) # 2026-02-15

# startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix.
print("Zain".startswith("Z")) # True
print("Zain".startswith("z")) # False
# endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix
print("zain".endswith('n')) # True
print("zain".endswith('a')) # False

# find(substring): Returns the index of the first occurrence of substring, or -1 if it doesn't find one.
print("Zain Ul Islam".find("Ul")) # 5
print("Zain Ul Islam".find("khan")) # -1

# count(substring): Returns the number of times a substring appears in a string.
print("hi,how are you? Where are you from?".count("are")) # 2
print("hi,how are you? Where are you from?".count("o")) # 4
print("hi,how are you? Where are you from?".count("z")) # 0

