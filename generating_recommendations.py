from movie_management import movie_catalog
from add_new_movies import *

def gen_recs():
    print(f"All genres: {genre_set}")
    pref_genres = input("Enter your preferred genre from the above set: ")
    print()
    list1 = []
    for movie in movie_catalog:
        if movie["genre"] == pref_genres:
            list1.append(movie["title"])
    return list1

