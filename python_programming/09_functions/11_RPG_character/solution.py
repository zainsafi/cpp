full_dot = '●'
empty_dot = '○'

def create_character(name,strenght,intelligence,charisma):

    if not isinstance(name,str):
        return 'The character name should be a string'
    
    if name == '':
        return 'The character should have a name'
    
    if len(name) > 10:
        return 'The character name is too long'
    
    if ' ' in name:
        return 'The character name should not contain spaces'
    
    if (not isinstance(strenght,int) or
        not isinstance(intelligence,int) or
        not isinstance(charisma,int)):
        return 'All stats should be integers'
    
    if (strenght < 1 or
        intelligence < 1 or
        charisma < 1):
        return 'All stats should be no less than 1'
    
    if (strenght > 4 or
        intelligence > 4 or
        charisma > 4):
        return 'All stats should be no more than 4'
    
    if (strenght + intelligence + charisma) != 7:
        return 'The character should start with 7 points'
    
    return (name + '\n' + 
            "STR " + (full_dot * strenght) + empty_dot * (10 - strenght) + '\n' +
            "INT " + (full_dot * intelligence) + empty_dot * (10 - intelligence) + '\n' +
            "CHA " + (full_dot * charisma) + empty_dot * (10 - charisma)
            )

# Calling the create_character function
print(create_character('Zain',3,1,3))
    
    # You can also use these alternative logics
    # This is called a generator expression. It behave like a loop
    # if not all(isinstance(stat, int) for stat in (strength, intelligence, charisma)):
    #     return "All stats should be integers."
    
    # if not all(stat >= 1 for stat in (strength, intelligence, charisma)):
    #     return "All stats should be no less than 1."
    
    # if not all(stat <= 4 for stat in (strength, intelligence, charisma)):
    #     return "All stats should be no more than 4."