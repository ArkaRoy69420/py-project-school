# CODE TO CALCULATE DISTANCE USING s = ut + (1/2)at^2

def calculateDistance(u: float, t: float, a: float): 
  return f"{u * t + ((1/2) * a * pow(t, 2))} units"

while True: # use loop for continuous iteration until the user opts out of the loop 👍
  print("\033[32mprogram calculates the distance traveled by an object given its initial velocity, time, and acceleration. \033[31m[ALL HAS TO BE IN SI UNITS!]\033[0m")
  U = float(input("Enter initial velocity (u): "))
  T = float(input("Enter time taken (t): "))
  A = float(input("Enter acceleration of the body (a): "))

  distanceTraveled = calculateDistance(U, T, A)

  # \033 [34m for blue color, \033 [0m - reset colors
  print(f"\033[34m{distanceTraveled} distance has been travelled by the body.\033[0m")  

  userContinueOrNot = input("Would you like to continue the calculator? (y/n)").lower() # lower it for cases of capital inputs
  
  while userContinueOrNot != "y" and userContinueOrNot != "n": # catch unknown input cases
    userContinueOrNot = input("Sorry I did not understand, please enter \"y\" or \"n\"")

  if userContinueOrNot == "n": # exit if n, else continue.
    print("Exited by user.")
    break;
