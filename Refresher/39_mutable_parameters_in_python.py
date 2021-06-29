from typing import List, Optional


class Student:
	def __init__(self, name: str, grades: Optional[List[int]] = None): #This is bad!
		self.name = name
		self.grades = grades or []

	def take_exam(self, result):
		self.grades.append(result)


bob = Student("Bob")
Rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(Rolf.grades)