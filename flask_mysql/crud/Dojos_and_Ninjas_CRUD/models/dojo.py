from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

Class Dojo:

def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

    self.ninjas = []
@classmethod
def get_all(cls):

    query = "SELECT * FROM dojos"

    result =  connectToMySQL('dojo_ninjas').query_db(query)

@classmethod
def save(cls, data):

    query = "INSERT INTO dojos(name) VALUE(%(name)s)"

    result =  connectToMySQL('dojo_ninjas').query_db(query, data)

    return result 





