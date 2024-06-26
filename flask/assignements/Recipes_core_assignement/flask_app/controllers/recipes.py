from flask_app import app
from flask import render_template, request, redirect, session
from flask import flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


@app.route('/recipes')
def dashboard():
    if 'user_id' not in session:
        flash("You must be logged in to access the dashboard.")
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    logged_user = User.get_by_id(data)
    recipes = Recipe.get_all()
    print(recipes)
    return render_template("dashboard.html", logged_user = logged_user , recipes = recipes) 

@app.route('/recipes/new')
def add_recipe_page():
    logged_user = User.get_by_id({'id': session['user_id']})
    return render_template('add_recipe.html', logged_user = logged_user)

 
@app.route('/recipes/edit/<int:id>')
def edit_page(id):
    data = {'id': id}
    recipe = Recipe.get_by_id(data)
    logged_user = User.get_by_id({'id': session['user_id']})
    return render_template('edit_recipe.html', recipe = recipe, logged_user = logged_user)

@app.route('/recipes/<int:id>')
def show_recipe_page(id):
    recipe = Recipe.get_by_id({'id': id})
    return render_template("show_recipe.html" , recipe = recipe)


@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    data = {'id': id}
    recipe = Recipe.get_by_id(data)
    if recipe.user.id == session['user_id']:
        Recipe.delete(data)
    
    return redirect('/recipes')

# Post methods

@app.route('/recipes/add', methods = ['POST'])
def create_recipe():
    data = request.form
    print(data)
    if Recipe.validate_create(data):
        Recipe.create(data)
        return redirect('/recipes')
    
@app.route('/recipes/update', methods = ['POST'])
def update_recipe():
        data = request.form
        Recipe.update(data)
        print(Recipe.update(data))
        return redirect('/recipes')