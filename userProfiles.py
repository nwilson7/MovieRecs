class UserProfile:
    def __init__(self, username):
        self.username = username
        self.preferred_genres = set()
        self.rated_movies = {}

    def add_genre(self, genre):
        self.preferred_genres.add(genre)

    def get_preferred_genres(self):
        return self.preferred_genres

    def __str__(self):
        return (f"UserProfile(username={self.username},"
                f"preferred)genres={list(self.preferred_genres)},"
                f"rated_movies={self.rated_movies}")