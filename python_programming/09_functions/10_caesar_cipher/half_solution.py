# str.maketrans() str.maketrans() method takes two strings of equal length and 
# returns a translation table that maps each character of the first string with 
# the corresponding character of the second string. Each character in the translation 
# table is stored as a Unicode ordinal, a number that uniquely identifies the character.
# Then you use .translate() to apply that mapping to a string

# half_solution

def caesar(text,shift):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # shift = 5
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # translation_table = str.maketrans(alphabet, shifted_alphabet)
    # To handle the remaining upper case alphabets
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    # print(translation_table) # print the table

    # text = 'hello world'
    # encrypted_text = text.translate(translation_table)
    # print(encrypted_text)

    return text.translate(translation_table)

encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)