# One solution is to initialize res as an empty string in 
# the enclosing scope, which is within outer_func. 
# Then within inner_func, make res a non-local variable with the nonlocal keyword:

def outerfunc():
    msg = "Hello World!"
    res = ""  # Declare res in the enclosing scope

    def innerfunc():
        nonlocal res # Allow modification of an enclosing variable
        res = "How are you?"
        print(msg) # Accessing msg from outer_func()

    innerfunc()
    print(res) # Now res is accessible and modified

outerfunc()

# Output:
# Hello there!
# How are you?