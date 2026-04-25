# some bad practices related to lamda function

# assigning lambda to variable => bad practice
numbers = [1, 2, 3, 4, 5]

square = lambda x: x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]

# This defeats the purpose of using anonymous functions. In this case, you should 
# use a regular function i-e
def square(num):
    return num ** 2

squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]

# COMPLEX LAMBDA (NOT GOOD STYLE) => bad practice

result = (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3) # works but not readable
print(result)  # 14

# better readable version
def calculate_expression(x):
    if x > 0:
        return x**2 + 2*x - 1
    else:
        return x**3 - x + 4

print(calculate_expression(3))  # 14


