# filter(): used to select elements based on a condition (returns iterable)
# syntax: filter(function, iterable) 
# function → A function that returns True or False
# iterable → A sequence like list, tuple, set, etc.
# It returns a filter object (iterator) containing only elements for which the function returns True.
# you can also use lamda function instead but it will be studied later

# Example 1: Selecting even numbers from a list
def check_even(number):
    # if number % 2 == 0:
    #     return True
    # else:
    #     return False
    # or in short you can also do it like this
    return number % 2 == 0

numbers = [1,2,3,4,5,6,7,]
result = filter(check_even,numbers)
print(list(result))

# printing those words whose length is greater than 4
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']
def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']


print()


# map(): used to transform (modify) each element of an iterable.
# syntax: map(function, iterable)
# function → A function applied to each element
# iterable → Sequence (list, tuple, etc.)
# Returns a map object (iterator) containing transformed values.

# Example 1: square of list numbers
numbers = [0,1,2,3,4,5]
def square(n):
    return n * n

squared_numbers = list(map(square,numbers))
print(squared_numbers) # [0, 1, 4, 9, 16, 25]


# Example 2: Converting temperature in celcius to fahrenheit
celsius = [0, 10, 20, 30, 40]
def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]


print()


# sum(): used to calculate total of elements in an iterable
numbers = [5, 10, 15, 20]

# basic sum
total = sum(numbers)
print(total)  # 50

# sum() with start value (positional argument) which sets the initial value for the summation.
total = sum(numbers, 10)
print(total)  # 60
print(sum(numbers,100)) # 150

# You can also use the start argument as a keyword argument i-e
total = sum(numbers, start=10)
print(total)  # 60 same result
