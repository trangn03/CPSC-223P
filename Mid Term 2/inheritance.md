# Inheritance
- Parent class: class being inherited from, also called base class
- Child class: class that inherits from another class, also called derived class
1. Create a Parent Class
    ```js
    class Person:
        def __init__(self, fname, lname):
            self.firstname = fname
            self.lastname = lname
        def printname(self):
            print(self.firstname, self.lastname)
    # Use the Person class to create an object, and then execute the printname method:
    x = Person("John", "Doe")
    x.printname()

    # Output
    John Doe
    ```
2. Create a Child Class
    ```js
    class Person:
        def __init__(self, fname, lname):
            self.firstname = fname
            self.lastname = lname
        def printname(self):
            print(self.firstname, self.lastname)
    class Student(Person):
        pass
    x = Student("Mike", "Olsen")
    x.printname()

    # Output
    Mike Olsen
    ```
3. Add the __init__() fuction
    ```js
    class Person:
        def __init__(self, fname, lname):
            self.firstname = fname
            self.lastname = lname
        def printname(self):
            print(self.firstname, self.lastname)
    class Student(Person):
        def __init__(self, fname, lname):
            Person.__init__(self, fname, lname)
    x = Student("Mike", "Olsen")
    x.printname()

    # Output
    Mike Olsen
    ```
4. Use the super() function
    ```js
    class Person:
        def __init__(self, fname, lname):
            self.firstname = fname
            self.lastname = lname
        def printname(self):
            print(self.firstname, self.lastname)
    class Student(Person):
        def __init__(self, fname, lname):
            super().__init__(self, fname, lname)
    x = Student("Mike", "Olsen")
    x.printname()

    # Output
    Mike Olsen
    ```