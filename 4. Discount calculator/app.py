# PROGRAM FOR CALCULATING DISCOUNT ON AN ITEM
import re
from math import floor

def calcDiscount(CP: float, discountPercent: float): 
  amtAfterDiscount = ((100-discountPercent)/100) * CP

  # eliminate the decimal point and 0 from the number [if there is]
  numbersAfterDecimal = re.findall(r"[0-9]\.(\d+)", amtAfterDiscount.__str__())
  if numbersAfterDecimal[0] == "0":
    amtAfterDiscount = floor(amtAfterDiscount)
  
  return f"₹{amtAfterDiscount}"

print("\033[32mThis program calculates the price of an item after discount [Provided the discount percentage!]\033[0m")

cp = float(input("Enter the cost price [CP]: "))
d_percent = float(input("Enter the discount%: "))

print(f"Selling price or price after discount: {calcDiscount(cp, d_percent)}")