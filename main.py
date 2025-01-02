from add_new_movies import add_new_movies, movie_catalog, genre_set

def display_menu():
    print("\nWelcome to the Movie Recommendation System!")
    print("Choose an option:")
    print("1. View all movies")
    print("2. View all genres")
    print("3. Add a new movie")
    print("4. View recommendations")
    print("5. Exit")
    print("----------")
    ch = input("Enter your choice: ")
    match ch:
        case 1:
            print(movie_catalog)
        case 2:
            print(genre_set)
        case 3:
            print(handle_add_movie())
        case 4:
            pass
        case 5:
            exit()



def handle_add_movie():
    movie_title = input("Enter the movie title: ")
    movie_genre = input("Enter the movie genre: ")
    add_new_movies(movie_title, movie_genre)
    return f"Movie '{movie_title}' added successfully!"

display_menu()