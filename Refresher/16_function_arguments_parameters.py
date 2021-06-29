#01 Example
def add(x, y):
	result = x + y
	print(result)


add(5, 3)

#define the variable 1st example
def say_hello(name, surname):
	print("Hello!, {name} {surname}")


say_hello(surname="Bob", name="Smith")

#03 Example
def divide(dividend, divisor):
	if divisor != 0:
		print(dividend / divisor)

	else:
		print("You fool!")


divide(dividend=15, divisor=0)