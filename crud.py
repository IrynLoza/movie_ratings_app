"""CRUD operations."""

from model import db, User, Movie, Rate, connect_to_db

def create_user(user_name, email, password):
    """Create and return a new user."""

    user = User(user_name=user_name, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


if __name__ == '__main__':
    from server import app
    connect_to_db(app)