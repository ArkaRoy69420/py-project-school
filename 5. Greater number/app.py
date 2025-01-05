# CODE TO FIND THE GREATER NUMBER

print("\033[32mThis program compares and find the greater number. :)\033[0m")
def find_greater_number(num1: float, num2: float):
  if num1 > num2:
    return num1
  elif(num1 == num2):
    return num2 == num1
  else:
    return num2

NUM1 = float(input("Enter the first number: "))
NUM2 = float(input("Enter the second number: "))

greater_number = find_greater_number(NUM1, NUM2)

consoleMsg = "Both numbers are equal :/" if type(greater_number) == bool else f"The greater number out of the two is {greater_number} :)" 
print(consoleMsg)