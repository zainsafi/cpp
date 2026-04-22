# list comprehension: used to create a new list in a single line (loop + condition)
# combine a loop and condition directly within square brackets
# syntax: 
# [expression for item in iterable if condition] => just if condition
# [expression_if_true if condition else expression_if_false for item in iterable] => if-else

# normal way of using loop
even_numbers = []
for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)


# list comprehension (short and clean way)
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)


# list comprehension with if-else condition
numbers = [1, 2, 3, 4, 5]

result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result) # [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]


number_list = []
for num in range(21):
    if num % 2 == 0:
        number_list.append(num)

print(number_list)

even_numbers = [num for num in range(10) if num % 2 == 0]
print(even_numbers)

result = [(num,'even') if num % 2 == 0 else (num,'Odd') for num in range(15)]
print(result)

result = [(num,'Even') if num % 2 == 0 else (num,"Odd")]