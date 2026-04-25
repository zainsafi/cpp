# lambda function

# normal def function
def square(num):
    return num ** 2

print(square(4)) # 16

# lambda function => anonymous (no name function)
square_numbers = lambda num: num ** 2
print(square_numbers(6)) # 36

# Note: You can pass argument directly into the lambda function on the same line.
square_numbers = (lambda num: num ** 2)(7) # as here 6 is passed directly
print(square_numbers) # 49


# LAMBDA WITH filter()
original_numbers = [1,2,3,4,5]
even_numbers = list(filter(lambda num: num % 2 == 0,original_numbers))
print(even_numbers) 

# even_number = filter(lambda num: num % 2 == 0,original_numbers)
# print(list(even_number)) # Also correct but not good practice

# LAMBDA with map()

squared_numbers = list(map(lambda num: num ** 2, original_numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]

increment_ten = list(map(lambda num: num + 10,original_numbers))
print(increment_ten) # [11, 12, 13, 14, 15]

