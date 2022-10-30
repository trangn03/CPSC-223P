# Errors and Exceptions
1. try and except keywords to handle exceptions. Both keywords are followed by intended blocks
- try: block contains one or more statements which are likely to encounter an exception
- except: block are meant to handle the cause of the exception appropriately
    - ex 1 : try...except blocks
        ```js
        try:
            a=5
            b='0'
            print(a/b)
        except:
            print('Some error occurred.')
        print("Out of try except blocks.")

        # Output
        Some error occurred.
        Out of try except blocks.
        ```
    - ex 2: catch specific error type
        ```js
        try:
            a=5
            b='0'
            print (a+b)
        except TypeError:
            print('Unsupported operation')
        print ("Out of try except blocks")

        # Output
        Unsupported operation
        Out of try except blocks
        ```
    - ex 3: multiple except blocks
        ```js
        try:
            a=5
            b=0
            print (a/b)
        except TypeError:
            print('Unsupported operation')
        except ZeroDivisionError:
            print ('Division by zero not allowed')
        print ('Out of try except blocks')

        # Output
        Division by zero not allowed
        Out of try except blocks
        ```
2. else and finally: while the except block is executed if the exception occurs inside the try block, the else block gets processed if the try block is found to be exception free.
    ```js
    try:
        print('try block')
        x=int(input('Enter a number: '))
        y=int(input('Enter another number: '))
        z=x/y
    except ZeroDivisionError:
        print("except ZeroDivisionError block")
        print("Division by 0 not accepted")
    else:
        print("else block")
        print("Division = ", z)
    finally:
        print("finally block")
        x=0
        y=0
    print ("Out of try, except, else and finally blocks." )

    # Output case 1: normal case
    try block
    Enter a number: 10
    Enter another number: 2
    else block
    Division =  5.0
    finally block
    Out of try, except, else and finally blocks.

    # Output case 2: division by zero
    try block
    Enter a number: 10
    Enter another number: 0
    except ZeroDivisionError block
    Division by 0 not accepted
    finally block
    Out of try, except, else and finally blocks.

    # Output case 3: an uncaught exception
    try block
    Enter a number: 10
    Enter another number: xyz
    finally block
    Traceback (most recent call last):
        File "C:\python36\codes\test.py", line 3, in <module>
            y=int(input('Enter another number: '))
    ValueError: invalid literal for int() with base 10: 'xyz'
    ```
3. Raise an Exception
    - causes an exception to be generated explicitly
        ```js
        try:
            x=int(input('Enter a number upto 100: '))
            if x > 100:
                raise ValueError(x)
        except ValueError:
            print(x, "is out of allowed range")
        else:
            print(x, "is within the allowed range")
        
        # Output
        Enter a number upto 100: 200
        200 is out of allowed range
        Enter a number upto 100: 50
        50 is within the allowed range
        ```