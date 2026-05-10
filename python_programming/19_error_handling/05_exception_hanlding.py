# Exception handling is the process of catching and managing errors that occur during 
# the execution of a program, so your code doesn't crash unexpectedly.

# Main keywords used in python for exception hanlding are:
# try, except, else, finally

# 1. try + except
# Code that may cause error goes inside try block
# If error happens, Python jumps to except block
print("try + except")
try:
    result = 10 / 0

except ZeroDivisionError:
    print("You cannot divide by zero.")

# 2. try + except + else
# else block runs ONLY if no exception occurs
print("\ntry + except + else")
try:
    result = 10 / 2

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Division successful:", result)


# 3. finally BLOCK
# finally block ALWAYS runs whether exception occurs or not
print('\nFinally block')
try:
    file = open("example.txt", "w")
    file.write("Hello")

except Exception:
    print("Something went wrong.")

finally:
    print("finally block always runs.")
    file.close()


# 4. handling multiple exceptions
# Different errors can be handled separately
print('\nHandlin multiple Exception')
try:
    number = int("abc")
    result = 10 / number

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# 5. USING 'as e'
# 'e' stores actual error object/message
print('\nUsing as e')
try:
    result = 1 / 0

except ZeroDivisionError as e:
    print("Error message ->", e)


# 6. MULTIPLE EXCEPTIONS IN ONE BLOCK
# Tuple can be used to catch multiple errors together
print('\nMultiple Exception in one block')
try:
    number = int(input("Enter a number: "))
    result = 10 / number

except (ValueError, ZeroDivisionError) as e:
    print("Error occurred ->", e)
else:
    print("No error occurred")


# 7. GENERIC EXCEPTION
# Exception catches almost every error
# Useful but should not always be overused
print('\nGeneric Exception')
try:
    my_list = [1, 2, 3]
    print(my_list[10])

except Exception as e:
    print("Something went wrong ->", e)


# 8. realistic example
# Safe calculator program
print('\nCalculator program')
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ValueError:
    print("Please enter valid integers.")

except ZeroDivisionError:
    print("Second number cannot be zero.")

else:
    print("Result =", result)

finally:
    print("Calculator program ended.")


