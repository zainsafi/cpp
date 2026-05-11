# raise statement in python
# The raise statement is used to manually trigger exceptions.
# It allows programmers to create custom errors and control program flow.

# basic raise statement
# Here we manually raise a ValueError
# if age is negative.
print('\n----- basic raise statement -----')
def check_age(age):

    if age < 0:
        raise ValueError("Age cannot be negative")

    return age


try:
    print(check_age(-5))

except ValueError as e:
    print("Error ->", e)



# raise with custom message instead of using default one

def divide(a, b):

    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")

    return a / b


try:
    print(divide(10, 0))

except ZeroDivisionError as e:
    print("Caught error ->", e)


# re-raising exception: raise without arguments re-raises the current exception.
print('\n----- re-raising an exception -----')

def process_data(data):

    try:
        result = int(data)
        return result * 2

    except ValueError:
        print("Logging error...")
        raise   # re-raises same exception


try:
    process_data("abc")

except ValueError:
    print("Handled at higher level")


