
# math module

# Import the whole module
import math

# To use anything from it, we use dot notation:
print("Square root of 36:", math.sqrt(36))
print("Value of pi:", math.pi)


# import with alias
# Sometimes module names are long, so we shorten them
import math as m

# Now we use 'm' instead of 'math'
print("Using alias (m):", m.sqrt(49))


# import specific functions
# Instead of importing everything, we can import only what we need
from math import sqrt, pow

# Now we can use them directly (no math. prefix)
print("sqrt(25):", sqrt(25))
print("5^2 using pow:", pow(5, 2))


# import with alias (specific)
# You can also rename individual functions
from math import sqrt as square_root

print("Using renamed function:", square_root(64))


# import everything (not recommended)

# This imports ALL functions into current namespace
# It works, but can cause confusion or conflicts
from math import *

print("Using * import:", sqrt(81), pow(3, 3))

