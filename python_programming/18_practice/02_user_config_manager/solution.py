test_settings = {'theme': 'light'}

# add_setting()
def add_setting(settings,pair):
    key,value = pair

    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value

    return f"Setting '{key}' added with value '{value}' successfully!"

# update_setting()
def update_setting(settings,pair):
    key,value = pair

    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

# delete_setting()
def delete_setting(settings,key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"

# view_setting()
def view_settings(settings):
    
    if settings == {}:
        return "No settings available."
    
    result = "Current User Settings:\n"

    for key,value in settings.items():
        result += f"{key.capitalize()}: {value}\n"

    return result

print(view_settings(test_settings))


print(add_setting(test_settings,('THEME','light')))
print(add_setting(test_settings,('volume','high')))

print(update_setting({'theme': 'light'}, ('theme', 'dark')))
print(update_setting({'theme': 'light'}, ('volume', 'high')))
# print(update_setting(test_settings,('theme','light')))
# print(update_setting(test_settings,('volume','high')))


print(delete_setting({'theme': 'light'},'theme'))

print(view_settings(test_settings))
