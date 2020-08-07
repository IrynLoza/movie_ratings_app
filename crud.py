"""CRUD operations."""

from model import db, User, Movie, Rate, connect_to_db
from datetime import datetime

def create_user(user_name, email, password):
    """Create and return a new user."""

    user = User(user_name=user_name, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie   

def create_rate(user, movie, rate):
    """Create and return a new rate.""" 

    rate = Rate(user=user, movie=movie, rate=rate)

    db.session.add(rate)
    db.session.commit()

    return rate    


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
