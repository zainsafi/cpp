# some methods used in the list are

numbers = [1, 2, 3,]
adding_numbers = [11,22,33]

# append() => add one element to the end of the list
numbers.append(4)
print(numbers) # [1, 2, 3, 4]
numbers.append([5,6,7]) # nested list [1, 2, 3, 4, [5, 6, 7]]
print(numbers)
numbers.append({5,6,7}) # set(random order) [1, 2, 3, 4, [5, 6, 7], {5, 6, 7}]
print(numbers)
numbers.append((5,6,7)) # tuple(immutable) [1, 2, 3, 4, [5, 6, 7], {5, 6, 7}, (5, 6, 7)]
print(numbers)
numbers.append(adding_numbers)  
print(numbers) # [1, 2, 3, 4, [5, 6, 7], {5, 6, 7}, (5, 6, 7), [11, 22, 33]]


# extend() => add multiple element individually to the end of the list and it takes iterables
# extend() NEVER cares about brackets [] { } ( )
numbers = [1, 2, 3,]
adding_numbers = [11,22,33]

# numbers.extend(4) # type error bcz not iterable
numbers.extend([5,6,7]) # [1, 2, 3, 4, 5, 6, 7]
print(numbers)
numbers.extend({5,6,7}) # [1, 2, 3, 4, 5, 6, 7, 5, 6, 7]
print(numbers)
numbers.extend((5,6,7)) # [1, 2, 3, 4, [5, 6, 7, 5, 6, 7, 5, 6, 7]
print(numbers)
numbers.extend(adding_numbers)  
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 5, 6, 7, 5, 6, 7, 11, 22, 33]

