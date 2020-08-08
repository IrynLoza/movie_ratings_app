"""CRUD operations."""

from model import db, User, Movie, Rate, connect_to_db
from datetime import datetime

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    
    return User.query.all() 

def get_user_by_id(user_id):

    return User.query.get(user_id)      

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie 

def get_movies():
    """Returns all movies"""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """Return movie by id"""

    return Movie.query.get(movie_id)          

def create_rate(user, movie, rate):
    """Create and return a new rate.""" 

    rate = Rate(user=user, movie=movie, rate=rate)

    db.session.add(rate)
    db.session.commit()

    return rate    


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
