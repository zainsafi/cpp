# Dictionaries are built-in data structures that store collections of key-value pairs

student_info = {'name': 'zain ul islam',
           'rollno': 11,
           'country': 'pakistan',
           'education': {
               'university': 'Islamia College Peshawar',
               'semester': 4
           }}

print((student_info))

print()

# updating / adding value to the dictionary using keys
student_info['rollno'] = 15 # updating rollno
print(student_info['rollno'])
student_info['education']['semester'] = 6 # updating semester
print(student_info['education']['semester'])
student_info['education']['section'] = 'A' # new value added
print(student_info['education']) # {'university': 'Islamia College Peshawar', 'semester': 6, 'section': 'A'}

print()

# accessing values using keys
print(student_info['name']) # zain ul islam
print(student_info['education']) # {'university': 'Islamia College Peshawar', 'Semester': '6th'}
print(student_info['education']['university']) # Islamia College Peshawar

print()

# get() => safe access (no error if key missing)
print(student_info.get('')) # None => no error 
print(student_info.get('name')) # zain ul islam
print(student_info.get('education')) # {'university': 'Islamia College Peshawar', 'semester': 6}
print(student_info.get('education',[])) # {'university': 'Islamia College Peshawar', 'semester': 6}
print(student_info.get('education').get('university')) # Islamia College Peshawar
print(student_info.get('educate','educate key doesn\'t exist')) # educate key doesn't exist

print()

# keys(),values() and items()
# accessing all the keys and values and key-value pairs
print((student_info.keys())) # dict_keys(['name', 'rollno', 'country', 'education'])
print(student_info.values())
# dict_values(['zain ul islam', 11, 'pakistan', {'university': 'Islamia College Peshawar', 'Semester': '6th'}])
print(student_info.items())
# dict_items([('name', 'zain ul islam'), ('rollno', 15), ('country', 'pakistan'), ('education', 
# {'university': 'Islamia College Peshawar', 'semester': 6, 'section': 'A'})])

print()

# dict() constructor 
student = dict([
    ('name','Asim'),
    ('rollno',31),
    ('education',dict([
        ('university','islamia college peshawar'),
        ('semester',6),
        ('section','A')])),
    ('city','peshawar'),
    ('contact',12534433)
])
print(student)

print()

# copying a dictionary
student_copy = student.copy() # i will print it at last

# pop() => remove key and return its value
print(student.pop('contact')) # 12534433
print(student['education'].pop('section')) 
student.pop('education') # peshawar
print(student) # {'name': 'Asim', 'rollno': 31, 'city': 'peshawar'}

print()

# popitem() => removes last inserted item
print(student.popitem()) # ('city', 'peshawar')
print(student) # {'name': 'Asim', 'rollno': 31}

# update() => update existing or add new keys
student.update({'age': 21})
print(student) # {'name': 'Asim', 'rollno': 31, 'age': 21}
student.update({'rollno': 50,'age': 22})
print(student) # {'name': 'Asim', 'rollno': 50, 'age': 22}

# clear() => removes all items
student.clear()
print(student) # {}

print()

print(student_copy)
# {'name': 'Asim', 'rollno': 31, 'education': {'university': 'islamia college peshawar', 'se
# mester': 6}, 'city': 'peshawar', 'contact': 12534433}