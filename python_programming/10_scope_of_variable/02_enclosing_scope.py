# Enclosing scope means that a function that's nested inside another 
# function can access the variables of the function it's nested within.

def outfunct():
    msg = "Hello World!"
    
    def innerfunct():
        print(msg) # accessing enclosing variable

    innerfunct()

outfunct() # Hello World!