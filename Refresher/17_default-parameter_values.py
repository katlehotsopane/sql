# y will be eqal to y 3 parameter

default_y = 3

# put the actual value in function 
def add(x, y=default_y):
	sum = x + y
	print(sum)


add(2)

default_y = 4
add(2)