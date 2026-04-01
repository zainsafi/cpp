# In python we can combine two strings with '+' which is called concatenation

first_name = "zain"
last_name = "Khan"
full_name = first_name + ' ' + last_name
print(full_name)

# You can't combine string with int or other types -> you will get typeerror
number = 4
# name_with_number = first_name + number // typeError
# print(name_with_number)
# so convert it first i-e
name_with_number = first_name + ' ' + 'lucky number is ' + str(number)
print(name_with_number)

# you can also use augmented assignment operator for concatenation.
last_name_with_number = last_name
last_name_with_number += ' ' + str(10) # similar to last_name_with_number = last_name_with_number + ' ' + str(10)
print(last_name_with_number)
