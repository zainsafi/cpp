# __name__ is a special built-in variable in Python
# (called a dunder variable).

# When a Python file is executed directly,
# Python sets the value of __name__ to "__main__".

# So, it works like the starting point of a program,
# similar to main() in C++.

# But if the Python file is imported as a module
# into another Python script, then the value of
# __name__ becomes the module name
# (usually the filename without the .py extension).


# ---------------- DUNDER VARIABLES ----------------

# Dunder = Double UNDERscore

# Dunder variables are special variables that
# start and end with double underscores (__).

# These variables and methods have predefined
# meanings to the Python interpreter.

# Examples:
# __name__
# __init__
# __str__
# __file__
# __doc__
# __dict__

# There are also dunder methods such as:
# __init__()
# __str__()

if __name__ == '__main__': 
    print(__name__)
    print(type(__name__))