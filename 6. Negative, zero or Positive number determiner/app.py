# CODE TO FIND IF THE PROVIDED NUMBER IS NEGATIVE, 0 OR POSItIVE

def checkNumber(n: int):
  if n < 0:
    return "Negative"
  elif n == 0:
    return "Zero"
  else:
    return "Positive"
    
print("\033[33mThis program finds if the provided integer is negative, zero or positive.\033[0m")

N = int(input("Enter a integer: "))

print(f"'{N}' is {checkNumber(N)}")