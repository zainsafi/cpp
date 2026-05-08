# 2. using pdb module 
# pdb = Python Debugger is a Built-in module for interactive debugging (means you can pause a 
# running program and interact with it while it is executing.)

import pdb
def divide(a, b):
    pdb.set_trace() # program pauses here and starts debugging
    return a / b

print(divide(10, 2))

# When execution reaches set_trace():
# Python opens debugger mode.

# If you enter help into the prompt, you'll see a list of commands you can use:

# common pdb commands:
# (Pdb) help

# Documented commands (type help <topic>):
# ========================================
# EOF    c          d        h         list      q        rv       undisplay
# a      cl         debug    help      ll        quit     s        unt      
# alias  clear      disable  ignore    longlist  r        source   until    
# args   commands   display  interact  n         restart  step     up       
# b      condition  down     j         next      return   tbreak   w        
# break  cont       enable   jump      p         retval   u        whatis   
# bt     continue   exit     l         pp        run      unalias  where    

# Miscellaneous help topics:
# ==========================
# exec  pdb

# Then you can use the commands to debug your code.

# For example, if you want to look at the type of elements throughout your code at that moment, you can use the whatis command:

# (Pdb) whatis a
# <class 'int'>
# (Pdb) whatis divide
# Function divide
# As you can see, by the time you run .set_trace(), the type of the parameter a is an integer, and divide is a function.

# Then to continue execution of your code, you can use the continue command, or one of its aliases, cont or c:

# (Pdb) continue
# 5.0
