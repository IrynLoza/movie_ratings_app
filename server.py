"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!

@app.route("/")
def homepage():
    """View Homepage"""
    
    return render_template("homepage.html")

@app.route("/movies")  
def all_movies():
    """View all movies"""
    
    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)

@app.route("/users")
def all_users():

    users = crud.get_users()

    return render_template('all_users.html', users=users)  

@app.route("/users/<user_id>")
def show_user(user_id):

    user = crud.get_user_by_id(user_id)

    return render_template('user_profile.html', user=user)      

@app.route("/movies/<movie_id>")
def movie_details(movie_id):

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)  

@app.route("/users", methods = ["POST"]) 
def add_data():

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
  
    if user:
        # flash('You can’t create an account with that email. Please, try again')
        if user.password == password:
            session['user'] = email #should be user.user_id 
            flash("Logged in!")
        else:
            flash('Wrong password. Try again')    
    else:
        crud.create_user(email, password)  
        flash('Your account was created successfully, you can now log in')  

    return redirect('/')


    

    # if password == 'let-me-in':   # FIXME
    #     session['current_user'] = username
    #     flash(f'Logged in as {username}')
    #     return redirect('/')

    # else:
    #     flash('Wrong password!')
    #     return redirect('/login')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
