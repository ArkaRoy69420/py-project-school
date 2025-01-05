# PROGRAM TO CALCULATE AVERAGE OF ODD NUMBERS IN A RANGE OF NUMBERS
print("\033[32mThis program finds the average of odd numbers in a provided range.\033[0m")
def calc(rangeStart: int, rangeEnd: int):
  oddNumbers = []
  for i in range(rangeStart, rangeEnd+1):
    if i % 2 == 1:
      oddNumbers.append(i)

  if oddNumbers.__len__() == 0:
    print("Invalid range.")
    exit()

  numberOfElements = oddNumbers.__len__()
  sumOfAllElements = 0
  for i in oddNumbers:
    sumOfAllElements += i

  avg = sumOfAllElements // numberOfElements

  return avg

RANGE_START = int(input("Enter the first number of range: "))
RANGE_END = int(input("Enter the last number of range: "))

print(f"Therefore, the average of odd numbers in the provided range of numbers is: {calc(RANGE_START, RANGE_END)}")