# PROGRAM TO FIND SUM OF ALL ELEMENTS IN AN list OF INT

print("\033[32mThis program finds the sum of all elements in an list.\033[0m")

array = [4, 2, 5 ,68, 45, 2, 7, 88, 34] # an example array

res = 0 # variable to store the sum of all elements
for element in array:
  res+=element

print(f"Sum of all elements in the array {array} is: {res}")