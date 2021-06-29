#loops now
friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in range(4):
	print(f"{friends} is my friend.")


#
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
	total += grade


print(total / amount)