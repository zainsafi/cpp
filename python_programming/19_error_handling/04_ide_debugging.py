# IDE Debugging Tools
# Many Integrated Development Environments (IDEs) offer advanced debugging tools, such as breakpoints, step execution, and variable inspection.

# Using VS Code Debugger
# If you use VS Code, you can set breakpoints in your code and run the debugger to pause execution at those points. Here's how to debug the same divide function:

# Step 1: Set up your code Create a file called main.py with the following content:

def divide(a, b):
    result = a / b
    return result

a = 10
b = 5
print(divide(a, b))
print(divide(15, 3))

# Step 2: Set a breakpoint
# Click in the gutter (left margin) next to line 2 (result = a / b) to set a breakpoint
# A red dot will appear, indicating the breakpoint is set

# Step 3: Start debugging
# Press F5 or go to Run > Start Debugging
# Select "Python File" when prompted
# The debugger will pause execution at your breakpoint

# Step 4: Inspect variables
# Hover over variables to see their current values
# Use the Variables panel on the left to see all local variables
# Use the Debug Console at the bottom to evaluate expressions

# Step 5: Step through code
# Use the debug toolbar to:
# Continue (F5): Resume execution until the next breakpoint
# Step Over (F10): Execute the current line and move to the next
# Step Into (F11): Enter into function calls
# Step Out (Shift+F11): Exit the current function

# IDE debugging tools provide a visual interface to examine the state of your program, making it easier to identify and fix issues compared to using print statements alone.

