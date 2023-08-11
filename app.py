from flask import Flask, render_template, request, redirect, url_for
from datamanager.json_data_manager import JSONDataManager

app = Flask(__name__)
data_manager = JSONDataManager('movies.json')  # Replace with your JSON file


@app.route('/')
def home():
    return "Welcome to MovieWeb App!"


@app.route('/users')
def list_users():
    users = data_manager.get_all_users()
    return render_template('users.html', users=users)


@app.route('/users/<int:user_id>')
def user_movies(user_id):
    user = data_manager.get_user_by_id(user_id)
    movies = data_manager.get_user_movies(user_id)
    return render_template('user_movies.html', user=user, movies=movies)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        new_user_name = request.form.get('user_name')
        data_manager.add_user(new_user_name)  # Implement the add_user method in the DataManager
        return redirect(url_for('list_users'))
    return render_template('add_user.html')


@app.route('/users/<int:user_id>/add_movie', methods=['GET', 'POST'])
def add_movie(user_id):
    if request.method == 'POST':
        new_movie_name = request.form.get('movie_name')
        # Fetch movie details from OMDb API and add the movie using DataManager
        data_manager.add_movie(user_id, new_movie_name)  # Implement the add_movie method in the DataManager
        return redirect(url_for('user_movies', user_id=user_id))
    return render_template('add_movie.html', user_id=user_id)


@app.route('/users/<int:user_id>/update_movie/<int:movie_id>', methods=['GET', 'POST'])
def update_movie(user_id, movie_id):
    user = data_manager.get_user_by_id(user_id)
    movie = data_manager.get_movie_by_id(user_id, movie_id)

    if request.method == 'POST':
        updated_movie_name = request.form.get('movie_name')
        # Update movie details using DataManager
        data_manager.update_movie(user_id, movie_id,
                                  updated_movie_name)  # Implement the update_movie method in the DataManager
        return redirect(url_for('user_movies', user_id=user_id))

    return render_template('update_movie.html', user=user, movie=movie)


@app.route('/users/<int:user_id>/delete_movie/<int:movie_id>', methods=['POST'])
def delete_movie(user_id, movie_id):
    # Delete the movie using DataManager
    data_manager.delete_movie(user_id, movie_id)  # Implement the delete_movie method in the DataManager
    return redirect(url_for('user_movies', user_id=user_id))


if __name__ == '__main__':
    app.run(debug=True)



