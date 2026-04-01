# string interpolation
# is the process of inserting variables and expressions into a string.
# Here you don't need to convert non-string types with the str() function

# method 1 
# f strings => lattest way and most recommended
name = 'zain ul islam'
age = 24
Qualification = 'Software Engineer'
message = f"My name is {name} and i am {age} years old"
print(message)

print(f"My name is {name} and i am a {Qualification}")

print(f"Sorry my age is {age - 1}")

num1 = 10
num2 = 5
print(f"The sum of {num1} and {num2} is {num1 + num2}")

# Method 2
# .format() method
print("My name is {} and My age is {}".format(name,age - 1)) 
#you can also name placeholder i-e
print("My name is {n} and My age is {a}".format(n = name,a = age - 1))


# Method 3
# % formatting (older style) 
gpa = 3.73
print("The sum of %d and %d is %d" %(num1,num2,num1 + num2))
print("My name is %s and my gpa is %f"%(name,gpa)) # six decimal places
print("My name is %s and my gpa is %.2f"%(name,gpa)) # Two decimal places now
