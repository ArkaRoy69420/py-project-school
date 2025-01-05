# CODE TO DETERMINE IF AN INDIVIDUAL IS ELIGIBLE TO VOTE.

print("\033[33mThis program determines eligibility for voting of an individual.\033[0m")

def isEligibleToVote(age: int):
  if (age >= 18):
    return True;
  else:
    return False;

age = int(input("Enter your age: "))

print(f"You are {"eligible" if isEligibleToVote(age) else "not eligible"} for voting")