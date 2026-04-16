# Unpacking values from a list is a technique used to assign values from a list to new variables

developer = ['Alice', 34, 'Rust Developer']
name,age,role = developer
print(name) # Alice
print(age) # 34
print(role) # Rust Developer

# extended unpacking
# If you need to collect any remaining elements from a list, you can use 
# the asterisk (*) operator i-e
developer = ('Alice', 34, 'Rust Developer')
name,*remaining = developer
print(name) # Alice
print(remaining) # [34, 'Rust Developer']

# you will get value error if number of variables didn't match the total numbers of list items
# name, age, job, city = developer # value error
