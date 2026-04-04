# is and isnot are identity operators

a = 9
b = a
c = 11
print(a is b) #true
print(b is a) #true
print(c is not b) #true
print(c is a) #false
print(a is not b) #false

a = "zain"
print(a is "zain") #true

# Example1 usage
x = None
if x is None:
    print("x is None")

# Example 2 Usage
a = [1, 2, 3]
b = a  # b is referring to the same object as a
c = [1, 2, 3]  # c is a new object with the same values

print(a is not b)  # False because both a and b refer to the same object
print(a is not c)  # True because a and c refer to different objects

#Difference between == and is
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True because their values are the same
print(a is b)  # False because they are different objects in memory
