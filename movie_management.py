class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def set_rating(self, new_rating):
        self.rating = new_rating

    def get_details(self):
        return f"Title: {self.title}, Genre: {self.genre}, Rating: {self.rating}"

movie1 = Movie("Inception", "Sci-Fi", 4)
movie2 = Movie("The Shawshank Redemption", "Drama", 4)
movie3 = Movie("The Dark Knight", "Action", 4)
movie4 = Movie("Pulp Fiction", "Action", 1)
movie5 = Movie("Forrest Gump", "Drama", 1)
movie6 = Movie("The Matrix", "Sci-Fi", 5)
movie7 = Movie("Interstellar", "Sci-Fi", 5)
movie8 = Movie("Parasite", "Thriller", 2)

# movie6.set_rating(4)
# print(movie6.get_details())
