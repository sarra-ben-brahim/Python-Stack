from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def read_users():
    return render_template("read_users.html", users = User.get_all())

@app.route('/user/new')
def new():
    return render_template("create_user.html")

@app.route('/user/create', methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect('/users')

@app.route('/users/<int:id>')
def show_user(id):
    data ={
        "id":id
    }
    return render_template("read_one_user.html", user = User.show(data))

@app.route('/users/edit/<int:id>')
def edit_user(id):
    data = {
        "id" : id
    }
    User.edit(request.form)
    return render_template("edit_user.html", user = User.show(data))

@app.route('/users/update', methods=['POST'])
def update():
    User.edit(request.form)
    return redirect('/users')

@app.route('/users/destroy/<int:id>')
def destroy(id):
    data = {
       "id" : id
    }
    User.destroy(data)
    return redirect('/users')
            