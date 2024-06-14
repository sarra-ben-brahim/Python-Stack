from flask import Flask, render_template, redirect, request
from users import Users
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def read_users():
    return render_template("read_users.html", users = Users.get_all())

@app.route('/user/new')
def new():
    return render_template("create_user.html")

@app.route('/user/create', methods=['POST'])
def create_user():
    print(request.form)
    Users.save(request.form)
    return redirect('/users')

@app.route('/users/<int:id>')
def show_user(id):
    data ={
        "id":id
    }
    return render_template("read_one_user.html", user = Users.show(data))

@app.route('/users/edit/<int:id>')
def edit_user(id):
    data = {
        "id" : id
    }
    Users.edit(request.form)
    return render_template("edit_user.html", user = Users.show(data))

@app.route('/users/update', methods=['POST'])
def update():
    Users.edit(request.form)
    return redirect('/users')

@app.route('/users/destroy/<int:id>')
def destroy(id):
    data = {
       "id" : id
    }
    Users.destroy(data)
    return redirect('/users')
            
if __name__ == "__main__":
    app.run(debug=True)

