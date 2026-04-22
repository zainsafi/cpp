# 2. zip(): used to combine multiple iterables (like lists, tuples etc) element by element

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]


# zip() converts multiple lists into pairs
print(list(zip(developers, ids))) # [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

# you can also do unzipping
zipped = [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]
names,id = zip(*zipped)
print(list(names))
print(id)

print()

# zip() used in loop
for name, id in zip(developers, ids):
    print(f'Name: {name} ID: {id}')
