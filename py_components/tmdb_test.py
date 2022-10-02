import tmdbsimple as tmdb
from datetime import *

tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5


genres = tmdb.Genres()
movie_genres = genres.movie_list()["genres"]


def  get_genres(id_list):
    if not id_list:
        return []
    result = []

    for id in id_list:
        for genre_data in movie_genres:
            if genre_data["id"] == id:
                result.append(genre_data["name"])
                break
    
    return result

def get_popular_movies():
    movies = tmdb.Movies()
    popular_movies = movies.popular(page=1)["results"]
    for movie_data in popular_movies:
        title = movie_data.get("title")
        release_date = datetime.strptime(movie_data.get("release_date"), "%Y-%m-%d").strftime("%Y.%B.%d.")
        vote_average = int(movie_data.get("vote_average") * 10)
        poster_path = "https://image.tmdb.org/t/p/w300" + movie_data.get("poster_path")
        genres = get_genres(movie_data.get("genre_ids"))
        print(title, genres)
        # print(title, release_date, vote_average, poster_path)
        # print(movie_data)
        # print((datetime.strptime(release_date, "%Y-%m-%d").strftime("%Y.%b.%d.")))

get_popular_movies()