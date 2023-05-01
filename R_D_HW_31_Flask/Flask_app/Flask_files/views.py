from Flask_files import app
import random, re
import werkzeug.exceptions
from flask import request, redirect, url_for, abort, render_template, session
from markupsafe import escape


app.secret_key = b'j33d0s'


@app.route("/")
def home():
    current = session.get('user')
    if current:
        return render_template('home.html', name=current)
    else:
        return redirect(url_for('login'))









# ----------------- USERS & USERS/ID routes -------------------
List_of_names = ['Alexei', 'Catherine', 'Ivan', 'Anna', 'Dmitry', 'Marina', 'Sergey', 'Julia',
                 'Nikita', 'Olga', 'Valeria', 'Artem', 'Margarita', 'Roman', 'Elena', 'Igor',
                 'Natalia', 'Pavel', 'Alice', 'Andrew', 'Oksana', 'Maxim', 'Victoria',
                 'Denis', 'Ludmila', 'Ruslan', 'Anastasia', 'Vladislav', 'Ksenia', 'Gleb']


@app.get('/users')
def users():
    current = session.get('user')
    if current:
        random_names = []
        for i in range(random.randint(1, 50)):
            random_names.append(random.choice(List_of_names))
        return render_template("users.html", content=random_names, user=current)
    else:
        return redirect(url_for('login'))


@app.get('/users/<int:user_id>')
def get_user_id(user_id):
    current = session.get('user')
    if current:
        if user_id % 2 == 0:
            return render_template('users_id.html', user_id=user_id, user=current)
        else:
            return 'Not found', abort(404)
    else:
        return redirect(url_for('login'))










# ------------------BOOKS & BOOKS/TITLE routes---------------
List_of_books = ['To Kill a Mockingbird', 'The Great Gatsby', '1984', 'Pride and Prejudice',
                 'One Hundred Years of Solitude', 'Brave New World', 'The Catcher in the Rye',
                 'Animal Farm', 'The Lord of the Rings', 'The Hitchhiker\'s Guide to the Galaxy',
                 'Wuthering Heights', 'The Picture of Dorian Gray', 'Frankenstein', 'Jane Eyre',
                 'The Adventures of Sherlock Holmes', 'Dracula', 'Fahrenheit 451',
                 'The Hobbit', 'The Time Machine', 'The War of the Worlds']


@app.get('/books')
def books():
    current = session.get('user')
    if current:
        random_books_list = []
        for i in range(random.randint(1, 50)):
            random_books_list += {random.choice(List_of_books)}
        return render_template("books.html", list_of_books= random_books_list, user=current)
    else:
        return redirect(url_for('login'))

@app.route('/books/<string:book_title>', methods=['GET'])
def book_name(book_title):
    current = session.get('user')
    if current:
        return render_template("books_id.html", book_title=book_title, user=current)
    else:
        return redirect(url_for('login'))








# ------------------ QUERY PARAMS ----------------------

@app.get('/params')
def get_params():
    current = session.get('user')
    if current:
        params = request.args
        return render_template("params.html", param=params, user=current)
    else:
        return redirect(url_for('login'))









# ------------------ LOGIN&LOGOUT GET&POST ----------------------
def validate_password(password):
    # Проверка наличия как минимум одной цифры, одной большой буквы и длины не менее 8 символов
    pattern = r'^(?=.*\d)(?=.*[A-Z]).{8,}$'
    match = re.match(pattern, password)
    if match:
        return True
    else:
        return False


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if len(request.form.get('username')) >= 5 and validate_password(request.form.get('password')):
            username = request.form.get('username')
            session['user'] = username
            return redirect(url_for('users'))
        else:
            return "Incorrect data", 400



@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))






# ------------------ CUSTOM EXCEPTIONS ----------------------


@app.errorhandler(werkzeug.exceptions.NotFound)
def default_404(e):
    return """<style>
                body {
                background-image: url("https://appmaster.io/api/_files/gLKT845SHV7cRiSsiFSDk6/download/");
                background-repeat: no-repeat;
                background-size: cover;
                background-position: center;
                height: 100vh;
                margin: 0;
            }
        </style>"""


@app.errorhandler(werkzeug.exceptions.InternalServerError)
def default_500(e):
    return """<style>
                    body {
                    background-image: url("https://cdn.dribbble.com/users/63485/screenshots/4331748/002_maze_beautiful_errors_final.gif");
                    background-repeat: no-repeat;
                    background-size: cover;
                    background-position: center;
                    height: 100vh;
                    margin: 0;
                }
            </style>"""