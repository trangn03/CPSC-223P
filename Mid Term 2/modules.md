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

