#how  distructing variables works
t = 5 , 11
x, y = t

print(x, y)


student_attendance = {"Rolf": 96, "Bob": 80, "Anne":100}

print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
	print(f"{student}: {attendance}")


#structuring
people =[("Bob", 42, "Mechanic"),("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for person  in people:
	print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

#tuple if three 
person = ("Bob", 42, "Mechanic")
name, _, Profession = person

print(name, Profession)


#0
*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)