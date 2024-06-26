from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
import re

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def register(cls, data):
        # encrypt the password
       encrypted_pasword = bcrypt.generate_password_hash(data['password'])
        # cast data to be mutable dict so we can modify the password
       data = dict(data) 
       data['password'] = encrypted_pasword
       
       # insert query
       query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
       results = connectToMySQL(DB).query_db(query, data)
       return results

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        if results:
            return cls(results[0])
        return None
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query, data)
        if results:
            return cls(results[0])
        return None
    
    @staticmethod
    def validate_register(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if len(data['first_name']) < 2:
            is_valid = False
            flash("First Name must be at least 2 characters long.", "register")
        if len(data['last_name']) < 2:
            is_valid = False
            flash("Last Name must ne at least 2 characters long.", "register")
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid Email.")
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash("Passwords must match.", "register")
        if user_in_db:
            is_valid = False
            flash("This user already exists in the database.", "register")
        
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if not user_in_db:
            is_valid = False
            flash("Email doesn't exist in our database.", "login")
        elif not bcrypt.check_password_hash(user_in_db.password, data['password']):
            is_valid = False
            flash("Incorrect Password", "login")
                
        return is_valid  