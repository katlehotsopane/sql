01 Example
movies_watched = {"The Matrix", "Ride Along", "Wrong Turn"}
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
	print(f"I've watched {user_movie} too!")

else:
	print("I haven't watched that yet.")