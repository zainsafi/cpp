# some other list methods

# insert() => add element at specific index
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)
print(numbers)  # [1, 2, 2.5, 3, 4, 5]


# remove() => remove first matching value
numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)
print(numbers)  # [10, 20, 30, 40, 50]


# pop() => remove by index (default last)
numbers = [1, 2, 3, 4, 5]
numbers.pop() # removes last element
print(numbers) 
numbers.pop(1) # remove the element at first index
print(numbers) # [1, 3, 4, 5]

# clear() => remove all elements from the list
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # []

# sort() => sort list in place (no new list)
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()
print(numbers)  # [1, 2, 19, 35, 41, 67]

# sorted() => returns new sorted list
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)
print(numbers) # original unchanged => [19, 2, 35, 1, 67, 41]
print(sorted_numbers)  # sorted copy => [1, 2, 19, 35, 41, 67]

# reverse() => reverse list in place
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# reversed() => returns a reversed iterator not a reversed list
# iterator simple analogy => An iterator is like:
#     a machine that gives values one at a time
#     not a full list stored in memory
numbers = [1, 2, 3, 4, 5]
# reversed_list = (reversed(numbers)) // not correct way
reversed_list = list((reversed(numbers))) # store the iterator values in a list
print(numbers) # original unchanged
print(reversed_list) # reversed copy


# index() => find first occurrence index
programming_languages = ['Rust', 'Java', 'Python', 'C++']
print(programming_languages.index('Java'))  # 1

