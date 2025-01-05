# PROGRAM TO FIND THE SUM OF FIRST "N" NUMBERS

print("\033[32mThis program finds the sum of first \"n\" specified.\033[0m")

def sum(n: int):
  result = 0
  for i in range(1, n+1):
    result += i;
  return result

N = int(input("Enter the value of 'n': "))

print(f"The sum of first {N} natural numbers is {sum(N)}.")