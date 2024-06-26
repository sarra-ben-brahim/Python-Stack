from flask_app import app
from flask_app.models.user import User
from flask import render_template, request, redirect, session


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['POST'])
def register():
    data = request.form
    if User.validate_register(data):
        User.register(data)
    return redirect('/')

@app.route('/login', methods = ['POST'])
def login():
    data = request.form
    if User.validate_login(data):
        user = User.get_by_email(data)
        session['user_id'] = user.id
        return redirect('/recipes')
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')