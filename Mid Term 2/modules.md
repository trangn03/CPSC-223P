# Modules
- Python interpreter has a number of built-in functions. They are always available for use in every interpreter session. 
1. Os module: Perform many tasks of operating system
    - mkdir(): create a new directory
        ```js
        >>> import os
        >>> os.mkdir("d:\\tempdir")
        ```
    - chdir(): change current working directory
        ```js
        >>> import os
        >>> os.chdir("d:\\temp")
        ```
    - getcdw(): returns name off current working directory
    - rmdir(): removes a specified directory either with absolute or relative path
    - listdir(): returns list of all files in specified directory
        ```js
        >>> os.listdir("c:\\Users")
        ['acer', 'All Users', 'Default', 'Default User', 'desktop.ini', 'Public']
        ```
2. Random module: difines various functions for handling randomization
    - random.random(): returns a float number between 0.0 to 1.0. Doesn't need any arguments
        ```js
        >>> import random
        >>> random.random()
        0.755173688207591
        ```
    - random.randint(): returns a random integer between the specified integers
        ```js
        >>> import random
        >>> random.randint(1,100)
        58
        >>> random.randint(1,100)
        91
        ```
    - random.randrange(): returns a random element from the range created by start, stop and step arguments
        ```js
        >>> random.randrange(1,10)
        2
        >>> random.randrange(1,10,2)
        3
        >>> random.randrange(0,101,10)
        40
    - random.choice(): returns a randomly selected element from a sequence object such as string, list or tuple.
        ```js
        >>> import random
        >>> random.choice('computer')
        'o'
        >>> random.choice([12,23,45,67,65,43])
        65
        ```
    - random.shuffle(): randomly reorders elements in a list.
        ```js
        >>> numbers=[12,23,45,67,65,43]
        >>> random.shuffle(numbers)
        >>> numbers
        [23, 12, 43, 65, 67, 45]
        ```
3. Math module: required mathematical functions
    - Pi
        ```js
        >>> import math
        >>> math.pi
        3.141592653589793
        ```
    - e
        ```js
        >>> math.e
        2.718281828459045
        ```
    - Trigonometric functions:
        - radians(): converts angle in degrees to radians.
            ```js
            >>> math.radians(30)
            0.5235987755982988
            ```
        - degrees():
            ```js
            >>> math.degrees(math.pi/6)
            29.999999999999996
            ```
        - sin, cos, tan
        - math.log(): returns natural logarithm of given number. Natural logarithm is calculated to the base e.
        - math.log10(): returns base-10 logarithm or standard logarithm of given number.
            ```js
            >>> math.log10(10)
            1.0
            ```
        - math.exp(): returns a float number after raising e (math.e) to given number. exp(x) is equivalent to e**x
            ```js
            >>> math.log10(10)
            1.0
            >>> math.e**10
            22026.465794806703
            ```
        - math.pow(): receives two float arguments, raises first to second and returns the result.
            ```js
            >>> math.pow(4,4)
            256.0
            ```
        - math.sqrt(): computes square root of given number
            ```js
            >>> math.sqrt(100)
            10.0
            ```
    - Representation functions:
        - ceil(): approximates given number to smallest integer greater than or equal to given floating point number.
        - floor(): function returns a largest integer less than or equal to given number
            ```js
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
        ```
    - OrderedDict() function: the order of insertion of keys in it whereas ordered dictionary object remembers the same
        ```js
        >>> d1={}
        >>> d1['A']=20
        >>> d1['B']=30
        >>> d1['C']=40
        >>> d1['D']=50
        ```
    - deque() function: supports append and pop operation from both ends of a list
        ```js
        >>> q=collections.deque([10,20,30,40])
        >>> q.appendleft(110)
        >>> q
        deque([110, 10, 20, 30, 40])
        >>> q.append(41)
        >>> q
        deque([0, 10, 20, 30, 40, 41])
        >>> q.pop()
        40
        >>> q
        deque([0, 10, 20, 30, 40])
        >>> q.popleft()
        110
        >>> q
        deque([10, 20, 30, 40])
        ```
5. Statustucs module: provides statistical functions
    - mean(): calculate arithmetic mean of numbers in a list
        ```js
        >>> import statistics
        >>> statistics.mean([2,5,6,9])
        5.5
        ```
    - median(): 
        ```js
        >>> import statistics
        >>> statistics.median([1,2,3,8,9])
        3
        >>> statistics.median([1,2,3,7,8,9])
        5.0
        ```
    - mode(): returnsmost repeated data point in the list
        ```js
        >>> import statistics
        >>> statistics.mode([2,5,3,2,8,3,9,4,2,5,6])
        2
        ```
    - stdev(): calculates standard deviation on given sample in the form of list.
        ```js
        >>> import statistics
        >>> statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5])
        1.3693063937629153
        ```
6. Time module
    - time(): returns current system time in ticks
        ```js
        >>> time.time()
        1544348359.1183174
        ```
    - localtime(): translates time in ticks in a time tuple notation
        ```js
        >>> tk=time.time()
        >>> time.localtime(tk)
        time.struct_time(tm_year=2018, tm_mon=12, tm_mday=9, tm_hour=15, tm_min=11, tm_sec=25, tm_wday=6, tm_yday=343, tm_isdst=0)
        ```
    - asctime(): returns a readable format of local time
        ```js
        >>> tk=time.time()
        >>> tp=time.localtime(tk)
        >>> time.asctime(tp)
        'Sun Dec  9 15:11:25 2018'
        ```
    - ctime(): returns string representation of system's current time
        ```js
        >>> time.ctime()
        'Sun Dec  9 15:17:40 2018'
        ```
    - sleep(): halts current program execution for a specified duration in seconds.
        ```js
        >>> time.ctime()
        'Sun Dec  9 15:19:14 2018'
        >>> time.sleep(20)
        >>> time.ctime()
        'Sun Dec  9 15:19:34 2018'
        ```