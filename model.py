"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# Replace this with your code!


def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_name = db.Column(db.String, unique=True, nullable=False)   #delete (50)                 
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    # ratings = a list of Rating objects

    def __repr__(self):
        return f'<User user_name={self.user_name} email={self.email}>' 
        #Remember when creating a test user to include user_name along with email and password

class Rate(db.Model):
    """A movie rating."""

    __tablename__ = "ratings"

    rate_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    rate = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id')) #changed from Str to Int
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id')) #changed from Str to Int
       
    movie = db.relationship('Movie', backref='ratings')
    user = db.relationship('User', backref='ratings')

    def __repr__(self):
        return f'<Rating rate_id={self.rate_id} rating={self.rate}>'
        
class Movie(db.Model):
    """Movies."""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String)                     
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster = db.Column(db.String)
    
    # ratings = a list of Rating objects
    
    def __repr__(self):
        return f'<Movie movie_id={self.movie_id} title={self.title}>'                    


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
