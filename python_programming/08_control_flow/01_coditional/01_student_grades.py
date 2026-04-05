#student grades
name = input("Enter the student name: ")
grades = input("Enter student grades: ")

if(grades >= 85 & grades < 100):
    print(name + " gets A Grade")
elif(grades >= 50 & grades < 85):
    print(name + "gets B Grade")
else: 
    print(name + "is fail")