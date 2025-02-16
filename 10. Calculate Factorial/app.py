# CODE TO CALCULATE THE FACTORIAL.
from math import factorial as f

print("\033[33mThis program finds factorial of a given number.\033[0m")

NUMBER = int(input("Enter a number whose factorial you want to find: "))

# example: factorial 5 is 1 x 2 x 3 x 4 x 5 = 120

numbersArray = []
res=1

# get the numbers to be multiplied into an array
for i in range(1, NUMBER+1):
  numbersArray.append(i)

# multiply the numbers and save it into "res" variable
for i in numbersArray:
  res = res *i

print(f"Factorial of {NUMBER} is {res}")
