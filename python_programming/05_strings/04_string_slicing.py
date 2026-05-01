# String slicing
# string slicing lets you extract a portion of a string
# basic syntax => string[start:stop]

my_name = 'Zain Ul Islam'
print(my_name[0:6]) # Zain U. The sixth index charcater will not be printed

print(my_name[:3]) # Zai
print(my_name[5:]) # Ul Islam
print(my_name[:])  # Zain Ul Islam

# step parameter is used to specify the increment between each index in the slice.
# basic syntax => string[start:stop:step]
# Case1: Positive Step (→ forward movement) => Condition: start < stop
# Case2: Negative Step (← backward movement) => Condition: start > stop

# Positive Step
print(f"{my_name[0:len(my_name):2]} \n")

# Negative Step
# A helpful trick you can do with the step parameter is to reverse a string
my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH
print(my_str[len(my_str)::-1]) # dlrow olleH
print(my_str[len(my_str):0:-1]) # dlrow olleH