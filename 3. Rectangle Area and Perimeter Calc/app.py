# PROGRAM TO CALCULATE THE AREA AND PERIMETER OF RECTANGLE
def calculateAreaOfRect(l: float, b: float): 
  area = l*b
  return f"{area} units"

def calcPerimeterOfRect(l: float, b: float):
  perimeter = 2*(l+b)
  return f"{perimeter} units"


print("\033[32mProgram calculates the area and perimeter of a rectangle. \033[31m[ALL VALUES HAS TO BE IN SAME UNITS!]\033[0m")

LENGTH = float(input("Enter length of rectangle (l): "))
BREADTH = float(input("Enter breadth of rectangle (b): "))

print(f"Area: {calculateAreaOfRect(LENGTH, BREADTH)}")
print(f"Perimeter: {calcPerimeterOfRect(LENGTH, BREADTH)}")