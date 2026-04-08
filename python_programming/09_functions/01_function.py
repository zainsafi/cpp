# A function is a reusable block of code that runs when it is called.

# Functions in Python are declared using the def keyword:
# def function_name(parameters):

# ---------------- Non-parameterized function ----------------

def hello():
    print("Hello World")

hello()  # Output: Hello World


# ---------------- Built-in Functions ----------------

# Python also has built-in functions like input() and int()

# input() → takes input from the user as a string
name = input("Enter your name: ")
print(name)


# int() → converts values into integers (removes decimal part if float)

print(int(3.14))   # 3
print(int("42"))   # 42
print(int(True))   # 1
print(int(False))  # 0