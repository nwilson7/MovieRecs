from add_new_movies import *
from movie_management import *
from generating_recommendations import *

def display_menu():
    while True:
        print("\nWelcome to the Movie Recommendation System!")
        print("Choose an option:")
        print("1. View all movies")
        print("2. View all genres")
        print("3. Add a new movie")
        print("4. View recommendations")
        print("5. Exit")
        print("----------")
        ch = int(input("Enter your choice: "))
        match ch:
            case 1:
                print(f"All the movies: {movie_catalog}")
            case 2:
                print(f"All the genres: {genre_set}")
            case 3:
                print(handle_add_movie())
            case 4:
                print(f"Your movie recommendations are: {gen_recs()}")
                break
            case 5:
                break
display_menu()