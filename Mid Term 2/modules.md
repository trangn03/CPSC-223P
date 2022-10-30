# Modules
- Python interpreter has a number of built-in functions. They are always available for use in every interpreter session. 
1. Os module: Perform many tasks of operating system
    - mkdir(): create a new directory
        ```json
        >>> import os
        >>> os.mkdir("d:\\tempdir")
        ```
    - chdir(): change current working directory
        ```json
        >>> import os
        >>> os.chdir("d:\\temp")
        ```
    - getcdw(): returns name off current working directory
    - rmdir(): removes a specified directory either with absolute or relative path
    - listdir(): returns list of all files in specified directory
        ```json
        >>> os.listdir("c:\\Users")
        ['acer', 'All Users', 'Default', 'Default User', 'desktop.ini', 'Public']
        ```
2. Random module: difines various functions for handling randomization
    - random.random(): returns a float number between 0.0 to 1.0. Doesn't need any arguments
        ```json
        >>> import random
        >>> random.random()
        0.755173688207591
        ```
    - random.randint(): returns a random integer between the specified integers
        ```json
        >>> import random
        >>> random.randint(1,100)
        58
        >>> random.randint(1,100)
        91
        ```
    - random.randrange(): returns a random element from the range created by start, stop and step arguments
        ```json
        >>> random.randrange(1,10)
        2
        >>> random.randrange(1,10,2)
        3
        >>> random.randrange(0,101,10)
        40
    - random.choice(): returns a randomly selected element from a sequence object such as string, list or tuple.
        ```json
        >>> import random
        >>> random.choice('computer')
        'o'
        >>> random.choice([12,23,45,67,65,43])
        65
        ```
    - random.shuffle(): randomly reorders elements in a list.
        ```json
        >>> numbers=[12,23,45,67,65,43]
        >>> random.shuffle(numbers)
        >>> numbers
        [23, 12, 43, 65, 67, 45]
        ```
3. Math module: required mathematical functions
    - Pi
    ```json
    >>> import math
    >>> math.pi
    3.141592653589793
    ```
    - e
    ```json
    >>> math.e
    2.718281828459045
    ```
    - Trigonometric functions:
        - radians(): converts angle in degrees to radians.
            ```json
            >>> math.radians(30)
            0.5235987755982988
            ```
        - degrees():
            ```json
            >>> math.degrees(math.pi/6)
            29.999999999999996
            ```
        - sin, cos, tan
        - math.log(): returns natural logarithm of given number. Natural logarithm is calculated to the base e.
        - math.log10(): returns base-10 logarithm or standard logarithm of given number.
            ```json
            >>> math.log10(10)
            1.0
            ```
        - math.exp(): returns a float number after raising e (math.e) to given number. exp(x) is equivalent to e**x
            ```json
            >>> math.log10(10)
            1.0
            >>> math.e**10
            22026.465794806703
            ```
        - math.pow(): receives two float arguments, raises first to second and returns the result.
            ```json
            >>> math.pow(4,4)
            256.0
            ```
        - math.sqrt(): computes square root of given number
            ```json
            >>> math.sqrt(100)
            10.0
            ```
    - Representation functions:




