graduated_students = ["students1", "students2", "students3", "students4", "students5"]
user_input = input("enter the name of the student: ")
if user_input in graduated_students:
    print(user_input + " graduated")
else:
    print(user_input + " not graduated")