from flask import Flask, request, jsonify
from flask_cors import CORS
from model import recommend_by_genre

app = Flask(__name__)
CORS(app)

@app.route("/recommend", methods=["POST"])
def recommend():

    genre=request.json["genre"]

    movies=recommend_by_genre(genre)

    return jsonify(movies)

if __name__=="__main__":
    app.run(debug=True)
@app.route("/trending")
def trending():

    top_movies = movies.sort_values(by="vote_average", ascending=False).head(8)

    results = []

    for _,row in top_movies.iterrows():

        poster,rating = get_movie_poster(row["title"])

        results.append({
            "title":row["title"],
            "poster":poster,
            "rating":rating,
            "genre":"Trending"
        })

    return jsonify(results)