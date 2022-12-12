# Name: Trang Ngo
# Date: 10/19/2022
# File Purpose: Classes and inheritance

class Person:
    # self object, first name string, last name string as positional parameter
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

# faculty inherits from person   
class Faculty(Person):
    # self object, first name, last name, department as position parameter
    def __init__(self, first_name, last_name, department):
        Person.__init__(self, first_name, last_name)
        self.department = department

# student inherits from person
class Student(Person):
    # self object, first name, last name as position parameter
    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name)
    
    # self object, class year string as position parameter
    def set_class(self, classyear):
        self.classyear = classyear

    # self object, major string as position parameter
    def set_major(self, major):
        self.major = major
    
    # self object, Faculty as position parameter
    def set_advisor(self, Faculty):
        self.advisor = Faculty