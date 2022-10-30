# Classes
1. Create a class --> Create Object
    ```js
    class MyClass:
        x = 5
    p1 = MyClass()
    print(p1.x)

    # Output
    5
    ```
2. The __init__() function
- always excecuted when the class is being initiated
- use the __init__() function to assign values to object properties
- called automatically every time the class is being used to create a new object
    ```js
    class Person:
        def __init__(self, name, age):
        self.name = name
        self.age = age  
    p1 = Person("John", 36)
    print(p1.name)
    print(p1.age)

    # Output
    John
    36
    ```
3. The __str__() function
- controls what should be returned when the class object is represented as a string.
- not set, the string representation of the object is returned
    ```js
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def __str__(self):
            return f"{self.name}({self.age})"    
    p1 = Person("John", 36)
    print(p1)

    # Output
    John(36)
    ```
4. Object Methods
- Objects can also contain methods. Methods in objects are functions that belong to the object.
    ```js
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def myfunc(self):
            print("Hello my name is " + self.name)
    p1 = Person("John", 36)
    p1.myfunc()

    # Output
    Hello my name is John
    ```
5. The self Parameter
- reference to the current instance of the class, and is used to access variables that belongs to the class.
    ```js
    class Person:
        def __init__(mysillyobject, name, age):
            mysillyobject.name = name
            mysillyobject.age = age
        def myfunc(abc):
            print("Hello my name is " + abc.name)
    p1 = Person("John", 36)
    p1.myfunc()

    # Output
    Hello my name is John
    ```
6. Modify Object Properties
    ```js
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def myfunc(self):
            print("Hello my name is " + self.name)
    p1 = Person("John", 36)
    p1.age = 40
    print(p1.age)
    
    # Output
    40
    ```
7. Delete Object Properties
    ```js
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def myfunc(self):
            print("Hello my name is " + self.name)
    p1 = Person("John", 36)
    del p1.age
    print(p1.age)
    
    # Output
    Traceback (most recent call last):
    File "demo_class7.py", line 13, in <module>
        print(p1.age)
    AttributeError: 'Person' object has no attribute 'age'
    ```
8. Delete Objects
    ```js
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def myfunc(self):
            print("Hello my name is " + self.name)
    p1 = Person("John", 36)
    del p1
    print(p1)
    
    # Output
    Traceback (most recent call last):
    File "demo_class8.py", line 13, in <module>
        print(p1)
    AttributeError: 'p1' is not defined
    ```
9. The pass Statement
    ```js
    class Person:
        pass
    # having an empty class definition like this, would raise an error without the pass statement
    ```