import random
from problem import *
# Quadratic Equation
print ("Quadratic Equation")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a == 0:
    print ("Input correct quadratic equation")
else:
    quadratic(a,b,c)
# Swap two variables
print ("Swap two variables")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
swap(a,b)
# Generate a random number
print ("Random number: ", random.randint(0,100))
# Convert kilometers to miles
print ("Convert kilometers to miles: ")
k = int(input("Enter kilometer: "))
ktom(k)
# Convert celsius to fahrenheit
print ("Convert celcius to fahrenheit")
c = int(input("Enter celcius: "))
ctof(c)
# Check leap year
year = int(input("Enter a year: "))
check_leap(year)
# Check prime number
print ("Check prime number")
number = int(input("Enter a number: "))
check_prime(number)
# Print the fibonacci sequence
print ("Fibonacci sequence")
fs = int(input("Enter the term you want: "))
fibonacci(fs)
# Find armstrong number in an interval
print ("Armstrong number")
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
armstrong(lower,upper)