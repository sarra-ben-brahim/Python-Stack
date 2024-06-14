from mysqlconnection import connectToMySQL

class Users:
    DB = 'mydb'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name, last_name, email) 
                VALUES (%(first_name)s, %(last_name)s, %(email)s);"""
        result = connectToMySQL('mydb').query_db(query, data) 
        return result
    
    @classmethod
    def show(cls, data):
        query = """SELECT * FROM users WHERE id = %(id)s """
        results = connectToMySQL('mydb').query_db(query, data)
        print(cls(results[0]))
        return cls(results[0]) 
    
    @classmethod
    def edit(cls, data):
        query = """UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id = %(id)s;"""
        return connectToMySQL('mydb').query_db(query, data)   
    
    @classmethod
    def destroy(cls, data):
        query = """DELETE FROM users WHERE id=%(id)s;"""  
        return connectToMySQL('mydb').query_db(query, data)