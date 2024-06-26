from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask_app import app
from flask_app.models.user import User
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under = data['under']
        self.date_cooked = data['date_cooked']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.user = None
        
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id ;"
        results = connectToMySQL(DB).query_db(query)
        if not results:
            return []
        recipes = []
        for row in results:
            recipe = cls(row)
            user_data = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['created_at'],
                'updated_at' : row['updated_at']
            }
            recipe.user = User(user_data)
            recipes.append(recipe)
        return recipes
    
    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query , data)
        if not results:
            return None
        recipe = cls(results[0])
        user_data = {
            'id' : results[0]['users.id'],
            'first_name' : results[0]['first_name'],
            'last_name' : results[0]['last_name'],
            'email' : results[0]['email'],
            'password' : results[0]['password'],
            'created_at' : results[0]['created_at'],
            'updated_at' : results[0]['updated_at']
        }
        recipe.user = User(user_data)
        return recipe
    
    @classmethod
    def create(cls, data):
        query = """INSERT INTO recipes (name, description, instruction, under, date_cooked, user_id) 
        VALUES (%(name)s, %(description)s, %(instruction)s, %(under)s, %(date_cooked)s, %(user_id)s);"""
        return connectToMySQL(DB).query_db(query , data)
    
    @classmethod
    def update(cls , data):
        query = "UPDATE recipes SET name = %(name)s , description = %(description)s ,instruction = %(instruction)s ,under = %(under)s, date_cooked = %(date_cooked)s, user_id = %(user_id)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)
    
    @classmethod 
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query , data)
        return result
    
    @staticmethod
    def validate_create(data):
        is_valid = True
        if len(data['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters long.", "add_recipe")
        if len(data['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters long.", "add_recipe")
        if len(data['instruction']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters long.", "add_recipe")
        return is_valid