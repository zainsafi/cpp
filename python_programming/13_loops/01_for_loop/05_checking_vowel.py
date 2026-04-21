# checking that a word has vowels or not
# else: Runs only if loop finishes normally mean it is executed only 
# when the loop is not terminated by a break statement.

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")
