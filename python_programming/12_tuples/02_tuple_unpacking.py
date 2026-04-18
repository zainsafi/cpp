# tuple unpacking
developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer

print(name) # Alice
print(age)  # 34
print(job)  # Rust Developer

# extended unpacking
developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer

print(name) # Alice
print(rest) # [34, 'Rust Developer']