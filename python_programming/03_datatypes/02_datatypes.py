# Integer (whole number)
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'> → Represents whole numbers without decimals
print(my_integer_var)

# Float (decimal number)
my_float_var = 4.50
print(type(my_float_var))  # <class 'float'> → Represents numbers with decimal points
print(my_float_var)

# String (text data)
my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'> → Represents a sequence of characters (text)
print(my_string_var)

# Boolean (True/False values)
my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'> → Represents logical values: True or False
print(my_boolean_var)

# Set (unordered collection of unique elements)
my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'> → Stores unique values, no duplicates allowed
print(my_set_var)

# Dictionary (key-value pairs)
my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'> → Stores data in key:value format
print(my_dictionary_var)

# Tuple (ordered, immutable collection)
my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'> → Similar to list but cannot be changed (immutable)
print(my_tuple_var)

# Range (sequence of numbers)
my_range_var = range(5)
print(type(my_range_var))  # <class 'range'> → Represents a sequence of numbers (commonly used in loops)
print(list(my_range_var))

# List (ordered, mutable collection)
my_list = [22, 'Hello world', 3.14, True]
print(type(my_list))  # <class 'list'> → Can store multiple items and can be modified (mutable)
print(my_list)

# NoneType (represents absence of value)
my_none_var = None
print(type(my_none_var))  # <class 'NoneType'> → Represents no value or null
print(my_none_var)