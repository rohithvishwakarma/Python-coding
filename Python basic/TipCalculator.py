bill = int(input("What is the total bill?\n"))
tip = int(input("Enter some tips\n"))
people = int(input("How many people are there?\n"))
total = ((tip/100*bill)+bill)/people
print(f"Total members are {people} and per head Rs.{total}")