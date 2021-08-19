student_heights = input("Input a list of student heights:\n").split()
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])  
print(student_heights)

total_height = 0
count = 0
for height in student_heights:
	total_height += height
	count += 1

avg_height = total_height/count
print(round(avg_height))
