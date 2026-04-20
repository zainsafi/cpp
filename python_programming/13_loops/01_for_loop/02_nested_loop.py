# Nested for loop
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

print()

# Nested for loop with condition
titles = ['Name','Roll No']
names = ['Zain','Ahmad','bilal']
roll_numbers = [9,4,7]
for title in titles:
    if title == 'Name':
        for name in names:
            print(f'{title}: {name}')
            
    if title == 'Roll No':
        for rollno in roll_numbers:
            print(f'{title}: {rollno}')