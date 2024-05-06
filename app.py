from flask import Flask, render_template, jsonify, request
import requests

my_app = Flask(__name__)

csv_data = 'static/data/movies.csv'
api_key = "cdef61e6863124de3864885e6d4455cf"

@my_app.route('/')
def home():
    return render_template('base.html')

@my_app.route('/movie_search')
def movie_search():
    query = request.args.get('query', '')  # Extract the query parameter from the URL
    url = f"https://api.themoviedb.org/3/search/movie?query={query}include_adult=true&language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer cdef61e6863124de3864885e6d4455cf"
    }
    response = requests.get(url, headers=headers)
    print("Response from TMDB:", response.text)
    movies = response.json().get('results', [])

    return render_template('api1.html', movies=movies)

if __name__ == '__main__':
    my_app.run(debug=True)