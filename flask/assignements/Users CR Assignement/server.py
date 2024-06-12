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
            
if __name__ == "__main__":
    app.run(debug=True)

