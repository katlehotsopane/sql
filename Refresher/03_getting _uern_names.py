#03 gertting user_input
size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = size_input / 10.8
print(f"{square_feet} sqaure feet is {square_metres:.2f} square metres.")