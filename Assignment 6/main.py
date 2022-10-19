# Name: Trang Ngo
# Date: 10/19/2022
# File Purpose: Output, Call all of the function in people module

from people import Faculty, Student

# variable hold a list of faculty
faculties = []
# variable hold a list of students
students = []

while True:
    print("      *** TUFFY TITAN STUDENT/FACULTY MAIN MENU ")
    print()
    print("1. Add faculty")
    print("2. Print faculty")
    print("3. Add student")
    print("4. Print student")
    print("9. Exit the program")
    print()
    # promp the user for the menu choice
    choice = int(input("Enter menu choice: ")) 
    print()

    # add faculty
    if (choice == 1):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        department = input("Enter department: ")
        f = Faculty(first_name, last_name, department)
        faculties.append(f)
        # or f.append(Faculty(first_name, last_name, department))
    
    # print faculty 
    elif (choice == 2): 
        print("======================= FACLUTY =======================")
        print("Record  Name                  Department")
        print("======  ====================  =========================")
        for i,x in enumerate(f):
            print(f'{str(i):8}{x.firstname+ " "+ x.lastname:22}{x.department:25}')
        print()
    
    # add student
    elif (choice == 3):
        first_name = input("Enter first name: " )
        last_name = input("Enter last name: ")
        class_year = input("Enter class year")
        major = input("Enter major: ")
        faculty_advisor = input("Enter faculty advisor: ")
        s = Student(first_name, last_name)
        s.set_class(class_year)
        s.set_major(major)
        s.set_advisor(faculties[faculty_advisor])
        students.append(s)

    # print student
    elif (choice == 4):
        print("===================================== STUDENTS ======================================")
        print("Name                  Class      Major                      Advisor")
        print("====================  =========  =========================  =========================")
        for i,x in enumerate(s):
            print(f'{x.firstname + " "+ x.lastname:22}{x.classyear:33}{x.major:60}{x.firstname+ " "+ x.lastname:87}')
        print()
    
    # exit the program
    elif (choice == 9):
        break
    else:
        print ("Invalid choice")