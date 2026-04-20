# continue statement is used to skip the current iteration of a loop and move onto the next iteration.

developer_names = ['Zain', 'Ahmad', 'Ali']

for developer in developer_names:
    if developer == 'Ahmad':
        continue # skip Ahmad and move to the next iteration i-e Ali
    print(developer) 