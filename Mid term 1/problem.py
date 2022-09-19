import math
import random
# Quadratic Equation
def quadratic(a,b,c):
    discrim = b * b - 4 * a * c
    square = math.sqrt(abs(discrim))
    if discrim > 0:
        print ("Real and different roots")
        print ((-b + square)/(2*a))
        print ((-b - square)/(2*a))
    elif discrim == 0:
        print ("Real and same roots")
        print (-b / 2*a)
    else: # discrim < 0
        print ("Complex roots")
        print(- b / (2 * a), " + i", square) 
        print(- b / (2 * a), " - i", square)
# Swap two variables
def swap (a,b):
    a,b = b,a
    print ("Value a after swapping: ", a)
    print ("Value b after swapping: ", b)
# Generate a random number
# Convert kilometers to miles
def ktom (k):
    convert = 0.621371
    miles = k * convert
    print ("Kilometers to miles: ", miles)
# Convert celsius to fahrenheit
def ctof (c):
    f = (c * 1.8) + 32
    print ("Celcius to Farenheit: ", f)
# Leap Year
def check_leap(year):
    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 ==0)):
        print ("Leap Year")
    else:
        print ("Not a leap year")

# Check prime number
def check_prime(number):
    if (number > 1):
        for i in range(2,number):
            if (number % i == 0):
                print (number, "is not a prime number")
                break
        else:
            print (number, "is a prime number")
    # If input number is <=, then not prime
    else:
        print (number, "is not a prime number")
# Print the fibonacci sequence
def fibonacci(fs):
    n1, n2 = 0, 1
    if fs == 1:
        print(n1)
    else:
        print(n1)
        print(n2)
        for i in range (2,fs):
            nth = n1 + n2
            n1 = n2
            n2 = nth
            print(nth)
# Find armstrong number in an interval
def armstrong (lower, upper):
    for num in range (lower, upper + 1):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if num == sum:
            print(num)