# CODE TO CALCULATE THE FACTORIAL.
from math import factorial as f

print("\033[33mThis program finds factorial of a given number.\033[0m")

NUMBER = int(input("Enter a number whose factorial you want to find: "))

print(f"Factorial of {NUMBER} is {f(NUMBER)}")
