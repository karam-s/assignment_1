the_names = ['a','b','c','d','e','f']

name_of_student= input("Enter the name of the student\
whose result you want to know:")
name_of_student=name_of_student.lower()
if (name_of_student in the_names):
    print ("the student is graduate.")
else:
    print ("the student is non-graduate.")

