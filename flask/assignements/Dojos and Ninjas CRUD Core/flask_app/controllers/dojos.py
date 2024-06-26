from flask import render_template , request , redirect
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def show_all():
    return render_template("index.html", dojos = Dojo.get_all())
    

@app.route('/create/dojo', methods=['POST'])
def register():    
    result = request.form
    Dojo.create(result)
    
    return redirect ('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data={
        "id": id
    }
    return render_template('dojo.html', dojo = Dojo.get_one_with_ninjas(data))

