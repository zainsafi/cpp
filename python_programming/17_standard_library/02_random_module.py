# random -> used to generate random values (numbers, choices, etc.)
import random

# returns a random float between 0.0 and 1.0 (0 and 1 not included)
print(random.random())


# randint(a, b)
# returns a random integer between a and b (inclusive)
print(random.randint(0,10)) 

# 3. randrange(start, stop, step)
# works like range() but returns a random value from it
print(random.randrange(10,40,2)) # 10 included but 40 not included

print()

# 4. choice(sequence)
# selects ONE random element from a list or sequence
names = ["Ali", "Zain", "Ahmed", "Usman"]
print(random.choice(names))
print(random.choices(names,k=2))

# shuffle(list)
# randomly rearranges elements of a list (changes original list everytime)
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(nums)

print()

# uniform(a, b)
# returns a random FLOAT between a and b
print(random.uniform(1,5)) # 1 and 5 not included

