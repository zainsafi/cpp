# Note: that outer functions cannot access variables defined within any nested functions

def outer_func():
    msg = 'Hello there!'
    # print(res) # can't access the local variable to inner function

    def inner_func():
        res = 'How are you?' # local to inner function
        print(msg)

    inner_func()

outer_func() # NameError: name 'res' is not defined

# solution is in next program