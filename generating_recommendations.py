from movie_management import *
from userProfiles import *
from add_new_movies import *


def gen_recs(user):
    list1 = []
    pref_genres = user.get_preferred_genres()
    for movie in movie_catalog:
        if movie["genre"] in pref_genres:
            list1.append(movie["title"])
    return list1
print(f"Movie recommendations for {user1.username}: {gen_recs(user1)}")
print(f"Movie recommendations for {user2.username}: {gen_recs(user2)}")

