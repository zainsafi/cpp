# string data type

name_1 = 'Hello'
print(name_1)

# Each character in a string has a position called index.
# first charcter is always at indext 0 
print(name_1[0]) # H
print(name_1[4]) # o
# negative indexing is not allowed in python.
# you can also get the last string as
print(name_1[-1]) # last index i-e o
print(name_1[-2]) # l

name_2 = 'Khan'
# concating two strings
print(name_1 + name_2)

print("123" + "1") # ---> it will print 1231 not 124 bcz both is consider as string

# There are two ways to skip the meaning of "" and '' in a string i-e 
# (1)use of ''' i-e use the opposite kind of quotes
# (2)use of \ 
print('''"Zain's lectures"''') 
print("Zain's Lectures") #or
print("\"Zain\'s lectures\"")
'''so if you want to skip the meaning of any thing or special character,use \ before it. you can also print
    \n by writting another \ before it '''

# print 5 times zain
print(5 * "zain ")

# multiple printings,pythone automatically add the space
print(name_1,name_2)

# Multi line string.
# you can use triple double quotes or triple sigle quotes
# to print multi line string 

multi_line_string_1 = """Hi
i am 
multi line 
string..""" 
print(multi_line_string_1)

multi_line_string_2 = '''i am 
also a multi line 
string
'''
print(multi_line_string_2)

# in operator => return a bolean
check = "how are you"
print("how" in check) # True
print('r' in check) # True
print('zain' in check) # False

# length of a string
print(len(check)) # 11
print(len("zain")) # 4

# Strings are immutable datatypes in python
# Immutable data types can't be modified or altered once they're declared.
# You can point their variables at something new, which is called reassignment,
# but you can't change the original object itself by adding, removing, or replacing any of its elements.
# You can reassign a different string to it but can't modify it i-e 

greeting1 = 'hi'
greeting1 = "hello" # this is ok
print(greeting1)
# but direct modification is not allow
# greeting2 = 'hi'
# greeting2[0] = 'H'
# # print(greeting2) # will give type error