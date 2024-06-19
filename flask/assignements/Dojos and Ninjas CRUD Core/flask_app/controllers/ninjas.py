from flask import render_template , request , redirect
from flask_app import app
from flask_app.models import dojo, ninja


@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html', dojos = dojo.Dojo.get_all())

@app.route('/create/ninja', methods=['POST'])
def save():
    result = request.form
    ninja.Ninja.create(result)
    
    return redirect ('/')