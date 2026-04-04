#Three logical operators i-e AND , OR and NOT
# The and and or operators are known as a short-circuit operators.

a,b = 5,4
print("Logical AND")
print(a > 4 and b < 10)
print(a > 4 and b < 3)

print("\nLogical OR")
print(a > 4 or b < 10)
print(a > 4 or b < 3)
print(a > 6 or b > 3 )

print("\nLogical NOT")
print(not(a))
c = False
print(not(c))