# Every value in Python is treated as either True (truthy) or False (falsy).
# Falsy values: None, False, Integer 0, Float 0.0, Empty strings ""
# Truthy values: Non-zero numbers, Non-empty strings
# You can check it by using bool() function

print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True