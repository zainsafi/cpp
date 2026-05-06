# some common python errors are
# SyntaxError       -> invalid syntax
# NameError         -> variable not defined
# TypeError         -> wrong data type operation
# IndexError        -> invalid index
# AttributeError    -> method doesn't exist
# ValueError        -> invalid value
# ZeroDivisionError -> divide by zero
# KeyError          -> missing dictionary key
# ModuleNotFoundError -> module not found
# IndentationError  -> wrong spacing/indentation


# 1. SyntaxError
# Happens when Python cannot understand the structure/syntax of your code.
# Common causes: missing brackets, missing colon, wrong indentation, invalid syntax
# Example:
# print("Hello"
# SyntaxError: '(' was never closed
# Fixed version:
print("Hello")


# 2. NameError
# Happens when you use a variable or function that has not been created/defined yet.
# Example:
# print(name)
# NameError: name 'name' is not defined
# Fixed version:
name = "Zain"
print(name)


# 3. TypeError
# Happens when operation is performed on incompatible data types.
# Example:
# result = 5 + "5"
# TypeError: unsupported operand type(s)
# Fixed version:
result = 5 + int("5")
print(result)


# 4. IndexError
# Happens when index does not exist in a list, tuple, or string.
numbers = [1, 2, 3]
# print(numbers[5])
# IndexError: list index out of range
# Fixed version:
print(numbers[2])


# 5. AttributeError
# Happens when object does not have the method/attribute you are trying to use.
num = 42
# num.append(5)
# AttributeError: 'int' object has no attribute 'append'
# append() works only with lists
# Fixed version
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)


# 6. ValueError
# Happens when data type is correct but value is invalid.
# Example:
# int("hello")
# ValueError: invalid literal for int()
# Fixed version:
print(int("25"))


# 7. ZeroDivisionError
# Happens when dividing by zero.
# Example:
# print(10 / 0)
# ZeroDivisionError: division by zero
# Fixed version:
print(10 / 2)


# 8. KeyError
# Happens when dictionary key does not exist.
student = {
    "name": "Zain",
    "age": 20
}
# print(student["grade"])
# KeyError: 'grade'
# Fixed version:
print(student.get("grade", "Key not found"))


# 9. ImportError / ModuleNotFoundError
# Happens when Python cannot find module.
# import not_existing_module
# ModuleNotFoundError
# Correct example:
import math
print(math.sqrt(25))


# 10. IndentationError
# Happens when indentation/spaces are wrong.
# Example:
# if True:
# print("Hello")
# IndentationError
# Fixed version:
if True:
    print("Correct indentation")

