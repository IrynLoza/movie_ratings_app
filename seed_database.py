"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. 
    title = movie['title']
    overview = movie['overview']
    poster_path = movie['poster_path']

    # Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    release_date = datetime.strptime(movie['release_date'], "%Y-%m-%d")

    # TODO: create a movie here and append it to movies_in_db
    movie_database = crud.create_movie(title, overview, release_date, poster_path)
    #call the function from crud.py to create movies using data
    #in movies.json


    movies_in_db.append(movie_database)

for n in range(10):
    email = f'user{n}@test.com'
    password = 'test' 

    # TODO: create a user here
    user = crud.create_user(email, password) 

    # TODO: create 10 ratings for the user
    for i in range(10):
        random_movie = choice(movies_in_db)
        rate = randint(1, 5)

        crud.create_rate(user, random_movie, rate)        