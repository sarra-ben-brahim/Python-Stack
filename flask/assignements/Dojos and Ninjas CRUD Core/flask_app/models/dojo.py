from flask_app.config.mysqlconnection import DB, connectToMySQL
from .ninja import Ninja


class Dojo :
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    
    @classmethod
    def create(cls, data):
        query = """INSERT INTO dojos (name) VALUES (%(name)s);"""
        result = connectToMySQL(DB).query_db(query, data)
        return result
    
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM dojos;"""
        results = connectToMySQL(DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_one_with_ninjas(cls, data):
        query = """SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id=%(id)s;"""
        results = connectToMySQL(DB).query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for d in results:
            n = {
                'id' : d['ninjas.id'],
                'first_name' : d['first_name'],
                'last_name' : d['last_name'],
                'age' : d['age'],
                'created_at' : d['created_at'],
                'updated_at' : d['updated_at']                
            }
            dojo.ninjas.append(Ninja(n))
        return dojo
        
    
    