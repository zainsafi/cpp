# LOOPING OVER DICTIONARIES

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}


# 1. LOOP OVER VALUES

for price in products.values():
    print(price)
# 990, 600, 250, 70


# 2. LOOP OVER KEYS

# method 1
for product in products.keys():
    print(product)

# method 2 (shortcut)
for product in products:
    print(product)
# Laptop, Smartphone, Tablet, Headphones


# 3. LOOP OVER KEY-VALUE PAIRS

for item in products.items():
    print(item)
# ('Laptop', 990), ...


# unpacking key and value
for product, price in products.items():
    print(product, price)


# 4. MODIFY VALUES (e.g. 20% discount)

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)
# {'Laptop': 792, 'Smartphone': 480, ...}

print()

# 5. USING enumerate() WITH DICTIONARY
# The enumerate () function returns an enumerate object, which assigns an 
# integer to each key-value pair
# You can start the counter from any number, but by default, it starts from 0.

# enumerate keys
print("Enumerating items")
# Here enumerate() function assigns an integer to each key, so we get tuples with the integer 
# and the key. Same for values and items
for product in enumerate(products):
    print(product) 
print()
# you can assign these values to separate loop variables i-e 
for index, product in enumerate(products):
    print(index, product) # or
for index,product in enumerate(products.keys()):
    print(index,product)

print()

# enumerate values
print("Enumerating values")
for product in enumerate(products.values()):
    print(product)
print()
for index, price in enumerate(products.values()):
    print(index, price)

print()

# enumerate key-value pairs
print("Enumerating items")
for item in enumerate(products.items()):
    print(item)
for index, item in enumerate(products.items()):
    print(index, item)

print()

# unpack everything
print('unpacking everything')
for index, (product, price) in enumerate(products.items()):
    print(index, product, price)

print()

# enumerate with custom start
print("enumerate with custom start")
for index, (product, price) in enumerate(products.items(), 1):
    print(index, product, price)