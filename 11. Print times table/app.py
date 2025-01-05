# CODE TO PRINT TIMES TABLE

print("\033[33mThis program prints times table of a number provided.\033[0m")

def timesTable(num: int, limit: int = 10): 
  timesTableArray = []
  for i in range(1, limit + 1):
    product = num*i;
    timesTableArray.append(f"{num} x {i} = {product}")

  return timesTableArray

number = int(input("Enter a number: "))
limit = input("Enter the limit till which you want the table: ")

if limit and limit.isdigit():
  limit = int(limit)

timesTableArray = timesTable(number, limit) if limit else timesTable(number)

for tt_element in timesTableArray:
  print(tt_element)