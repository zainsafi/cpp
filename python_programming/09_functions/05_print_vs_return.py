def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

x = add_print(2, 3)    # prints 5 but returns None
y = add_return(2, 3)   # returns 5

print("x:", x)
print("y:", y)