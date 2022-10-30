# Input and Output
1. Output
    - str.format(): make the output more presentable
    - {} acts as placeholders
        ```js
        # Here we take two variables and do certain operations with it.                                                 
        x = 3
        y = 12
        mul = x * y
        print('The value of x is {} and y is {}'.format(x, y))
        # Here we are specifying the order of the variables.
        print('{2} is the multiplication of {0} and {1}'.format(x, y, mul))
        # We can even use keyword arguments to format strings.
        print('Hey! Welcome to {company}. In this article we will learn about {language}'.format(company='Scaler', language='Python'))

        # Output
        The value of x is 3 and y is 12
        36 is the multiplication of 3 and 12
        Hey! Welcome to Scaler. In this article we will learn about Python
        ```
    - We can use the old % method
        ```js
        add = 5 + 6
        print("The new number after addition is %d" % add)

        # Output
        The new number after addition is 11
        ```
2. Input
    - take input from the user
        - ex 1: 
            ```js
            name = input("Enter your first name: ")
            print("Hey! " + name)

            # Ouput
            Enter your first name: Prajit
            Hey! Prajit
            ```
        - ex 2:
            ```js
            # Here we will take an integer as input from the user.
            age = int(input("Enter your age: "))
            new = age + 1
            name = input("Enter your name: ")
            print("Hey! " + name + " Next year you will be " + str(new))

            # Output
            Enter your age: 19
            Enter your name: Ayush
            Hey! Ayush Next year you will be 20
            ```
        - ex 3:
            ```js
            # Here we will take two numbers as input from the user.
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            mul = num1 * num2
            print("The multiplication of num1 & num2 is: %.2f" % mul)

            # Output
            Enter first number: 2.5
            Enter second number: 2
            The multiplication of num1 & num2 is: 5.00
            ```
            "%.2f": printed should be upto 2 decimal places