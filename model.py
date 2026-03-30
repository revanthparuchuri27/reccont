import pandas as pd
import requests
import json

API_KEY = "f3ca9c5347b230a906da57999ac21d48"

movies = pd.read_csv("dataset/tmdb_5000_movies.csv")

def get_movie_poster(title):

    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"

    try:
        data = requests.get(url).json()

        if data["results"]:
            poster_path = data["results"][0]["poster_path"]
            rating = data["results"][0]["vote_average"]

            if poster_path:
                poster = "https://image.tmdb.org/t/p/w500" + poster_path
            else:
                poster = ""

            return poster, rating

    except:
        pass

    return "", 0
def recommend_by_genre(genre):

    results=[]

    for i,row in movies.iterrows():

        try:
            genres=json.loads(row["genres"])
        except:
            continue

        genre_list=[g["name"] for g in genres]

        if genre in genre_list:

            poster,rating=get_movie_poster(row["title"])

            results.append({
                "title":row["title"],
                "poster":poster,
                "rating":rating,
                "genre":genre
            })

        if len(results)>=8:
            break

    return results