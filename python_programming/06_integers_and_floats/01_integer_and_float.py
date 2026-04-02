first_number = 15
second_number = 5
print(f"Integer addition: {first_number + second_number}")
print(f"Integer subtraction: {first_number - second_number}")
print(f"Integer multiplication: {first_number * second_number}")
print(f"Integer division: {first_number / second_number}")
print(f"Integer modulus: {first_number % second_number}")

# Floor division divides two numbers and returns the greatest integer less than or equal to the result.
# This is done with the double forward slash operator (//):
print(f"Integer Floor division: {first_number // second_number}")

# Exponentiation raises a number to the power of another, 
# and is done with the double asterisk operator (**):
print(f"Integer exponentation: {2**10}") # 2 power 10 = 1024


first_decimal = 9.9
second_decimal = 0.1
print(f"float addition: {first_decimal + second_decimal}")
print(f"float subtraction: {first_decimal - second_decimal}")
print(f"float multiplication: {first_decimal * second_decimal}")
print(f"float division: {first_decimal / second_decimal}")
print(f"float modulus: {first_decimal % second_decimal}")
print(f"float floor division: {first_decimal // second_decimal}")
print(f"float exponentation: {first_decimal ** second_decimal}")


# integer to float
print(float(9))
# integer to string
print(type(str(110)))
# string to integer
print(type(int('119')))
print(int('119')) # and same you can done for float
# float to integer
print(int(11.999))

# round() Rounds a number to the specified number of decimal places. By default 
# this function rounds to the nearest integer, and returns a whole number with no decimal places
print(round(29.2348763)) # 29
print(round(12.568,1)) # 12.6 => rounded upto one decimal
print(round(12.568,2)) # 12.57 => rounded upto two decimal

# abs(): returns the absolute(positive) value of a number
print(abs(-29)) # 29

#pow
print(pow(2,10)) # 1024 => # Equivalent to 2 ** 10
print(pow(2,3,5)) # 3 => Equivalent to (2 ** 3) % 5

# Augmented assigment: It combines a binary operation with an assignment in one step.
# Every operator can use an augmented assignment
num_1 = 10 
num_1 -= 5
print(num_1) # 5
power = 2
power **= 10 
print(power) # 1024

# There are no ++ and -- operators in python as in c++ rather for it you will have
# do e.g x = x + 1 or x += 1
# Writing ++x in Python just applies the unary plus twice, and does not increment anything e.g
my_var = 5
print(+my_var)   # 5 //unary plus like writting +5 or 5 both are same
print(++my_var)  # 5
print(+++my_var) # 5
my_var += 1 # incremented
print(my_var) # 6
