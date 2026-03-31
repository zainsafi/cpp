# typecasting or type conversion
length = len("zain ul islam ")
print("your name has " + str(length) + " characters") 
'''we have converted the int data type of length to string by using str() function bcz string
 and integer can't be added to each other.this is called type casting'''
print(type(length))
new_length = str(length)
print(type(new_length))
#similarly we can change between other datatypes
print(10 + 10) #integer
print("10" + "10") #string
print(int("10") + int("10")) #integer
print(int("10") + float("10")) #float

