movie_catalog = [
    {
        "title": "Inception",
        "genre": "Sci-Fi",
    },
    {
        "title": "The Shawshank Redemption",
        "genre": "Drama",
    },
    {
        "title": "The Dark Knight",
        "genre": "Action",
    },
    {
        "title": "Pulp Fiction",
        "genre": "Action",
    },
    {
        "title": "Forrest Gump",
        "genre": "Drama",
    },
    {
        "title": "The Matrix",
        "genre": "Sci-Fi",
    },
    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
    },
    {
        "title": "Parasite",
        "genre": "Thriller",
    }
]

genre_set = set()
for movie_details in movie_catalog:
    genre_set.add(movie_details["genre"])

def add_new_movies(title, genre):
    movie_catalog.append({"title": title, "genre": genre})

flag = True
while flag:
    ask1 = input("Do you want to add a new movie (y/n): ").lower()
    if ask1 == 'y':
        movie_title = input("Enter the movie title: ")
        movie_genre = input("Enter the movie genre: ")
        add_new_movies(movie_title, movie_genre)
        flag=False
    elif ask1 == 'n':
        flag=False
    else:
        flag=True
print(f"Movie catalog: {movie_catalog}")
