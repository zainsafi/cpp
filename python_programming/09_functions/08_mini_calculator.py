# mini caclulator
def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    choice = input("Enter + or *: ")

    if choice == "+":
        return a + b
    else:
        return a * b

result = calculator()
print("Result:", result)
