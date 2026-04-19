# slice operator (:) => works same as lists

fruits = ('Apple', 'Banana', 'Mango', 'Orange', 'Grapes')

print(fruits[0:3]) # ('Apple', 'Banana', 'Mango')
print(fruits[1:]) # ('Banana', 'Mango', 'Orange', 'Grapes')
print(fruits[:]) # ('Apple', 'Banana', 'Mango', 'Orange', 'Grapes')

print(fruits[::2]) # ('Apple', 'Mango', 'Grapes')

# move backward
print(fruits[::-1]) # ('Grapes', 'Orange', 'Mango', 'Banana', 'Apple')
print(fruits[::-3]) # ('Grapes', 'Banana')
print(fruits[2::-1]) # ('Mango', 'Banana', 'Apple')
print(fruits[3:1:-1]) # ('Orange', 'Mango')

# printing even and odd numbers
numbers = (1, 2, 3, 4, 5, 6)
print(numbers[1::2])  # (2, 4, 6)

numbers = (0, 1, 2, 3, 4, 5, 6)
print(numbers[1::2])  # (1, 3, 5)