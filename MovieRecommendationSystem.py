class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def set_rating(self, new_rating):
        self.rating = new_rating

    def get_details(self):
        return f"{self.title} ({self.genre}) - Rating: {self.rating}"


# Testing:
#
# m1 = Movie("xyz", "horror", "A")
# m1.set_rating('B')
# print(m1.get_details())
