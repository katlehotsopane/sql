import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit.
Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")

    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)

def print_movie_list(movies):
    print("-- Upcoming movies --")
    for movie in movies:
        print(f"{movie[0]} (on {movie[1]})")
    print("---- \n")

def prompt_show_watched_movies():
	username = input("Username: ")
	movies = database.get_watched_movies(username)
	if movies:
		print_movie_list("Watched", movies)
	else:
		print("That user has watched no movies yet!")

def prompt_watch_movie():
	username = input("Username: ")
	movies = database.get_watched_movies(username)
	print_movie_list("Watched", movies)

def prompt_search_movies():
	search_term = input("Enter partial movie title: ")
	return database.search_movies(search_term)

while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(upcoming=True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        movies = prompt_get_watched_movies()
        if movies:
            print_movie_list("Watched", movies)
        else:
            print("That user has watched no movies yet!")
    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        movies = prompt_search_movies()
        if movies:
            print_movie_list("Movies found", movies)
        else:
            print("Found no movies for that search term!")
    else:
        print("Invalid input, please try again!")