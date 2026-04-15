# Global scope refers to variables that are declared outside
# any functions or classes which can be accessed from anywhere in the program.

my_var = 100

def show_var():
    print(my_var)

show_var() # 100
print(my_var) # 100