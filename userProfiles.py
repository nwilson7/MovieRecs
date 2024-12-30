class UserProfile:
    def __init__(self, username):
        self.username = username
        self.preferred_genres = set()
        self.rated_movies = {}


    def add_genre(self, genre):
        self.preferred_genres.add(genre)

    def get_preferred_genres(self):
        return self.preferred_genres

    def get_details(self):
        return (f"Username = {self.username}\n"
                f"Preferred_genres = {self.preferred_genres}\n"
                f"Rated_movies = {self.rated_movies}")

    def rate_movie(self, movie, rating):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        self.rated_movies[movie] = rating

user1 = UserProfile("Abhishek")
user1.add_genre('Action')
user1.add_genre('Thriller')
user1.rate_movie('Inception', 1)
user1.rate_movie('Dark Knight', 5)


user2 = UserProfile("Nicholas")
user2.add_genre('Sci-Fi')
user2.add_genre('Action')
user2.rate_movie('Interstellar', 5)
user2.rate_movie('Parasite', 2)