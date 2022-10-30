# Modules
- Python interpreter has a number of built-in functions. They are always available for use in every interpreter session. 
1. Os module: Perform many tasks of operating system
    - mkdir(): create a new directory
        ```
        >>> import os
        >>> os.mkdir("d:\\tempdir")
        ```
    - chdir(): change current working directory
        ```
        >>> import os
        >>> os.chdir("d:\\temp")
        ```
    - getcdw(): returns name off current working directory
    - rmdir(): removes a specified directory either with absolute or relative path
    - listdir(): returns list of all files in specified directory
        ```
        >>> os.listdir("c:\\Users")
        ['acer', 'All Users', 'Default', 'Default User', 'desktop.ini', 'Public']
        ```
2. Random module: difines various functions for handling randomization
    - random.random(): returns a float number between 0.0 to 1.0. Doesn't need any arguments
        ```
        >>> import random
        >>> random.random()
        0.755173688207591
        ```
    - random.randint(): returns a random integer between the specified integers
        ```
        >>> import random
        >>> random.randint(1,100)
        58
        >>> random.randint(1,100)
        91
        ```
    - random.randrange(): returns a random element from the range created by start, stop and step arguments
        ```
        >>> random.randrange(1,10)
        2
        >>> random.randrange(1,10,2)
        3
        >>> random.randrange(0,101,10)
        40
    - random.choice(): returns a randomly selected element from a sequence object such as string, list or tuple.
        ```
        >>> import random
        >>> random.choice('computer')
        'o'
        >>> random.choice([12,23,45,67,65,43])
        65
        ```
    - random.shuffle(): randomly reorders elements in a list.
        ```
        >>> numbers=[12,23,45,67,65,43]
        >>> random.shuffle(numbers)
        >>> numbers
        [23, 12, 43, 65, 67, 45]
        ```
3. Math module: required mathematical functions
    - Pi
    ```
    >>> import math
    >>> math.pi
    3.141592653589793
    ```
    - e
    ```
    >>> math.e
    2.718281828459045
    ```
    - Trigonometric functions:
        - radians(): converts angle in degrees to radians.
            ```
            >>> math.radians(30)
            0.5235987755982988
            ```
        - degrees():
            ```
            >>> math.degrees(math.pi/6)
            29.999999999999996
            ```
        - sin, cos, tan
        - math.log(): returns natural logarithm of given number. Natural logarithm is calculated to the base e.
        - math.log10(): returns base-10 logarithm or standard logarithm of given number.
            ```
            >>> math.log10(10)
            1.0
            ```
        - math.exp(): returns a float number after raising e (math.e) to given number. exp(x) is equivalent to e**x
            ```
            >>> math.log10(10)
            1.0
            >>> math.e**10
            22026.465794806703
            ```
        - math.pow(): receives two float arguments, raises first to second and returns the result.
            ```
            >>> math.pow(4,4)
            256.0
            ```
        - math.sqrt(): computes square root of given number
            ```
            >>> math.sqrt(100)
            10.0
            ```
    - Representation functions:
        - ceil(): approximates given number to smallest integer greater than or equal to given floating point number.
        - floor(): function returns a largest integer less than or equal to given number
            ```
            >>> math.ceil(4.5867)
            5
            >>> math.floor(4.5687)
            4
            ```
        - sys module: provides functions and variables used to manipulate different parts of the Python runtime environment.
        - sys.argv: return list of command line arguments passed to a Python script
        - sys.exit: causes program to end and return to either Python console or command prompt. It is used to safely exit from program in case of exception.
        - sys.maxsize: returns the largest integer a variable can take.
        - sys.path: returns search path for all Python modules.
        - sys.stdin, sys.stdout, sys.stderr: interpreter for standard input, output and errors. stdin is used for all interactive input (Python shell). stdout is used for the output of print() and of input(). 
        - sys.version: displays a string containing version number of current Python interpreter.
4. Collections module
    - namedtuple() function: returns object of  a tuple subclass with named fields
        ```js
        >>> import collections
        >>> employee=collections.namedtuple('employee', [name, age, salary])
        To create a new object of this namedtuple
        >>> e1=employee("Ravi", 251, 20000)





