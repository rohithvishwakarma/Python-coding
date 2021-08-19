import random

names = input("Enter Everybodies name:\n")
bowl = names.split(",")
choice = random.randint(0,len(bowl)-1)
person = bowl[choice]

print(f"{person} is going to buy the meal today")

