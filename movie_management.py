class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def set_rating(self, new_rating):
        self.rating = new_rating

    def get_details(self):
        return f"Title: {self.title}, Genre: {self.genre}, Rating: {self.rating}"

all_movies = []
all_movies.append(Movie("Inception", "Sci-Fi", 4))
all_movies.append(Movie("The Shawshank Redemption", "Drama", 4))
all_movies.append(Movie("The Dark Knight", "Action", 4))
all_movies.append(Movie("Pulp Fiction", "Action", 1))
all_movies.append(Movie("Forrest Gump", "Drama", 1))
all_movies.append(Movie("The Matrix", "Sci-Fi", 5))
all_movies.append(Movie("Interstellar", "Sci-Fi", 5))
all_movies.append(Movie("Parasite", "Thriller", 2))

movie_catalog = []
for movie in all_movies:
    movie_catalog.append({"title": movie.title, "genre": movie.genre})
