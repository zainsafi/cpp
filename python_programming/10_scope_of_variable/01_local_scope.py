# vairable scope means where a variable can be accessed in the program
# To correctly determine scope, Python follows the LEGB rule, which stands for the following:
# Local scope (L), Enclosing scope (E), Global scope, (G) Built-in scope (B)

# local scope: means that a variable declared inside a function or class 
# can only be accessed within that function or class.

def my_func():
    my_var = 15 # Locally scoped to my_func
    print(my_var)
my_func() # 15
# print(my_var) # NameError: name 'my_var' is not defined

