from Flask_files import app
import random, re
import werkzeug.exceptions
from flask import request, redirect, url_for, abort
from markupsafe import escape



@app.route("/")
def home():
    return """
        <ul>
            <li><a href="/login">Login</a></li>
            <li><a href="/users">Users</a></li>
            <li><a href="/books">Books</a></li>
            <li><a href="/params">Param</a></li>
        </ul>
    """

# ----------------- USERS & USERS/ID routes -------------------
List_of_names = ['Alexei', 'Catherine', 'Ivan', 'Anna', 'Dmitry', 'Marina', 'Sergey', 'Julia',
                 'Nikita', 'Olga', 'Valeria', 'Artem', 'Margarita', 'Roman', 'Elena', 'Igor',
                 'Natalia', 'Pavel', 'Alice', 'Andrew', 'Oksana', 'Maxim', 'Victoria',
                 'Denis', 'Ludmila', 'Ruslan', 'Anastasia', 'Vladislav', 'Ksenia', 'Gleb']


@app.get('/users')
def users():
    random_names = []
    for i in range(random.randint(1, 50)):
        random_names.append(random.choice(List_of_names))
    return random_names


@app.get('/users/<int:user_id>')
def get_user_id(user_id):
    if user_id % 2 == 0:
        return f"<div>User id is {user_id}</div>", 200
    else:
        return 'Not found', abort(404)


# ------------------BOOKS & BOOKS/TITLE routes---------------
List_of_books = ['To Kill a Mockingbird', 'The Great Gatsby', '1984', 'Pride and Prejudice',
                 'One Hundred Years of Solitude', 'Brave New World', 'The Catcher in the Rye',
                 'Animal Farm', 'The Lord of the Rings', 'The Hitchhiker\'s Guide to the Galaxy',
                 'Wuthering Heights', 'The Picture of Dorian Gray', 'Frankenstein', 'Jane Eyre',
                 'The Adventures of Sherlock Holmes', 'Dracula', 'Fahrenheit 451',
                 'The Hobbit', 'The Time Machine', 'The War of the Worlds']


@app.get('/books')
def books():
    html_ul = '<ul>'
    for i in range(random.randint(1, 50)):
        html_ul += f'<li> {random.choice(List_of_books)} </li>'
    html_ul += '</ul>'
    return f'<div style=background red>{html_ul}</div>'


@app.route('/books/<string:book_title>', methods=['GET'])
def book_name(book_title):
    return f"<h3>{book_title.title()}</h3>"


# ------------------ QUERY PARAMS ----------------------

@app.get('/params')
def get_params():
    params = request.args
    table = '<table><tr><th>parameter</th><th>value</th></tr>'
    for key, value in params.items():
        table += f'<tr><td>{key}</td><td>{value}</td></tr>'
    table += '</table>'
    return table


# ------------------ LOGIN GET&POST ----------------------
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
        html_form = """
           <form method=POST action='/login'>
               <input type='string' name='username' placeholder="username" value="" />
               <input type='password' name='password' placeholder="password" value="" />
               <button type='submit'>Send form</button>
           </form>
           """
        return html_form, 200
    elif request.method == 'POST':
        if len(request.form.get('username')) >= 5 and validate_password(request.form.get('password')):
            return redirect(url_for('users'))
        else:
            return "Incorrect data", 400


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