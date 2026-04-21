# enumerate(): function keeps track of the index for an iterable and returns an enumerate object.

languages = ['Spanish', 'English', 'Russian', 'Chinese']

# basic loop (no index)
for language in languages:
    print(language)


# manual indexing 
index = 0
for language in languages:
    print(f'Index {index} and language {language}')
    index += 1


# enumerate() => automatic index tracking easier way
for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')


# enumerate() converted to list 
print(list(enumerate(languages))) 
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')] => tuple inside list


# enumerate() with start index
for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}')
