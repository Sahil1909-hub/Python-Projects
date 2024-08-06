# Making an empty student dictionary
student_list = { }

#function to add student and grade
def add_student(name, grade):
    student_list[name] = grade
    print(f"{name} student added successfully")
    print(f"{name} : {grade}")

#function to update 
def update_student(name, grade):
    if name in student_list:
        student_list[name] = grade
        print(f"{name} is updated with {grade} marks")

    else:
        print(f"{name} not in list")

#function to delete
def delete_student(name):
    if name in student_list:
        del student_list[name]
        print(f"{name} student deleted")
    else:
        print(f"{name} not in list")

#function to view
def view_student():
    if student_list:
        for name, grade in student_list.items():
        # student_list[name] = [grade]
          print(f"{name} : {grade}")
    else:
        print(f"{name} is not in the list")


# function to access the list
def main():
    while True:
        print("Student access managment system")
        print("Press 1. to add students in the list")
        print("Press 2. to update the student list")
        print("Press 3. to delete a student from the list")
        print("Press 4. to view the student list")
        print("Press 5. to exit()")

        choice = int(input("Enter you choice : "))

        if choice == 1:
           name = input("Enter the name: ")
           grade = int(input("Enter the grade: "))
           add_student(name,grade)

        elif choice == 2:
           name = input("Enter the name: ")
           grade = int(input("Enter the grade: "))
           update_student(name,grade)

        elif choice == 3:
           name = input("Enter the name: ")
           del student_list[name]
           delete_student(name)

        elif choice == 4:
           view_student()

        elif choice == 5:
           print("The program is closing,,,")
           break

        else:
           print("Invalid choice")

main()


        
    


        

    















