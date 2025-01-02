from movie_management import *

genre_set = set()
for movie_details in movie_catalog:
    genre_set.add(movie_details["genre"])

def add_new_movies(title, genre):
    movie_catalog.append({"title": title, "genre": genre})

def handle_add_movie():
    movie_title = input("Enter the movie title: ")
    for movie in movie_catalog:
        if movie_title == movie["title"]:
            print("Movie already exists in the catalog")
            return ""
    movie_genre = input("Enter the movie genre: ")
    add_new_movies(movie_title, movie_genre)
    return f"Movie '{movie_title}' added successfully!"
