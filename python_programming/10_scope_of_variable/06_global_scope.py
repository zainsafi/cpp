# if you want to make a locally scoped variable defined inside a function 
# globally accessible, you can use the global keyword
# you can also use global keyword to modify global variable

my_var1 = 7 # global variable

def show_vars():
    # declare the global variable first before using/modifying
    global my_var2 # creating a global variable
    global my_var1 # Allows modification of a global variable

    my_var2 = 20

    print(my_var1)
    print(my_var2)

    # my_var1 = 100 # Unbound local error
    # print(my_var1)

    my_var1 = 100 # now no error
    print(my_var1)

show_vars() # 7,20,100

# my_var_2 is now a global variable and can be accessed anywhere in the program
print(my_var2) # 20
