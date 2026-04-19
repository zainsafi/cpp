# some of the methods of the tuples are

# count() => counts how many times a value appears
print("count() method")
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages.count('Rust'))        # 2
print(programming_languages.count('JavaScript'))  # 0
numbers = (1,2,3,2,5,2,9)
print(numbers.count(2)) # 3
# print(programming_languages.count())  # TypeError (argument required)

print("index() method")
# index() => returns first index of value
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(programming_languages.index('Java'))  # 1
# If the specified item cannot be found, then Python raises a ValueError:
# print(programming_languages.index('JavaScript'))  # ValueError


# index() with start argument
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(programming_languages.index('Python', 3))  # 5

# index() with start and stop
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
print(programming_languages.index('Python', 2, 5))  # 2

# no sort() method in tuple

# sorted() => returns a new sorted LIST (not tuple)
print("sorted method()")
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted_tuple = sorted(numbers)
print(f"Original tuple: {numbers}")
print(f"Sorted tuple: {sorted_tuple}")

# sorted() with key => custom sorting
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(sorted(programming_languages)) # by default by name ['C++', 'Java', 'Python', 'Python', 'Rust', 'Rust']
print(sorted(programming_languages, key=len)) # by length ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']

# sorted() with reverse
print(sorted(programming_languages, reverse=True)) # ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']
print(sorted(programming_languages,key=len, reverse=True)) # ['Python', 'Python', 'Rust', 'Java', 'Rust', 'C++']
