# range(): used to generate a sequence of integers. 
# syntax: range(start, stop, step)
# by default start is 0

for num in range(5): # 5 end 
    print(num) # print  numbers from 0 to 4

print()

for num in range(1,5): # start = 1, end = 5
    print(num) # print  numbers from 1 to 4 

print()

# Step controls how much a variable increments or decrements in each iteration of a loop.

# printing even number
for num in range(0,21,2):
    print(num,end=' ') # printing in the same line with space at the end

print()

# printing odd number
for num in range(1,21,2):
    print(num,end=',') # printing in the same line with , at the end

print()

# range() => if you pass no argument or float numbers => TypeError
# for num in range():
#     print(num) # TypeError
# for num in range(3.15):
#     print(num) # TypeError

# printing numbers in decrementing order
for num in range(40,-1,-10):
    print(num,end=' ')

print() # you have to add it after using print with end to start printing in next line

# Note: you can also use range to create a list of integers 
number_list = list(range(0,11))
print(number_list)
number_list = list(range(0,11,2)) # even number list
print(number_list)