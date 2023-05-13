from flask_files import app, db
import random, re, werkzeug.exceptions, os
from flask import request, redirect, url_for, abort, render_template, session, flash
from .models import *

app.secret_key = os.getenv('SECRET_KEY')


@app.route("/")
def home():
    current = session.get('user')
    if current:
        return render_template('home.html', name=current)
    else:
        return redirect(url_for('login'))


# --------------------------------------PURCHASE-------------------------------

@app.route('/purchases')
def purchases():
    current = session.get('user')
    if current:
        purchases_query = db.session.query(Purchase)
        purchase_id = request.args.get('purchase_id')
        if purchase_id:
            purchases_query = purchases_query.filter_by(id=purchase_id)
        purchases = purchases_query.all()
        return render_template("purchases.html", purchases=purchases)
    else:
        return redirect(url_for('login'))



@app.route('/purchases/<int:purchase_id>')
def purchase_id(purchase_id):
    current = session.get('user')
    if current:
        id_purchase = db.session.execute(db.select(Purchase).where(Purchase.id == purchase_id)).scalars()
        print(id_purchase)
        if id_purchase:
            return render_template('purchase_id.html', purchase_id_html=id_purchase)
        else:
            return redirect(default_404)
    else:
        return redirect(url_for('login'))


# ----------------- USERS & USERS/ID routes -------------------
@app.route('/users', methods=['GET', 'POST'])
def users():
    current = session.get('user')
    if current:
        if request.method == 'GET':
            users_query = db.session.query(User)
            user_id = request.args.get('user_id')
            # users_info = [{'id': item.id, 'first_name': item.first_name, 'last_name': item.last_name, 'age': item.age} for item in users_query]
            if user_id:
                users_query = users_query.filter_by(id=user_id)
            result = users_query.all()
            return render_template("users.html", users=result, current_user=current)
        elif request.method == 'POST':
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            age = request.form.get('age')
            new_user = User(first_name=first_name, last_name=last_name, age=age)
            db.session.add(new_user)
            db.session.commit()
            flash('Пользователь добавлен')
            return redirect(url_for('users'))

    else:
        return redirect(url_for('login'))

    # @app.route('/purchases')
    # def purchases():
    #     current = session.get('user')
    #     if current:
    #         purchases_query = db.session.query(Purchase)
    #         purchase_id = request.args.get('purchase_id')
    #         if purchase_id:
    #             purchases_query = purchases_query.filter_by(id=purchase_id)
    #         purchases = purchases_query.all()
    #         return render_template("purchases.html", purchases=purchases)
    #     else:
    #         return redirect(url_for('login'))


@app.get('/users/<int:user_id>')
def get_user_id(user_id):
    current = session.get('user')
    if current:
        id_user = db.session.execute(db.select(User).where(User.id == user_id)).scalar()
        if id_user:
            return render_template("users_id.html", current_user=current, users=id_user, user_id=user_id)
        else:
            return redirect(default_404)
    else:
        return redirect(url_for('login'))






# ------------------BOOKS & BOOKS/TITLE routes---------------


@app.route('/books', methods=['GET', 'POST'])
def books():
    current = session.get('user')
    if current:
        if request.method == 'GET':
            books = db.session.execute(db.select(Book)).scalars()
            result = [{'id': item.id, 'title': item.title, 'author': item.author, 'year': item.year, 'price': item.price} for item in books]
            return render_template("books.html", books=result, current_user=current)
        elif request.method == 'POST':
            title = request.form.get('title')
            author = request.form.get('author')
            year = request.form.get('year')
            price = request.form.get('price')
            new_book = Book(title=title, author=author, year=year, price=price)
            db.session.add(new_book)
            db.session.commit()
            flash('Книга добавлена')
            return redirect(url_for('books'))
    else:
        return redirect(url_for('login'))



@app.route('/books/<int:book_id>', methods=['GET'])
def book_name(book_id):
    current = session.get('user')
    if current:
        one_book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        if one_book:
            return render_template("books_id.html", current_user=current, one_book=one_book)
        else:
            return redirect(default_404)
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