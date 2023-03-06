from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re	  
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    
    
    @classmethod
    def save_user(cls, data): #!CREATE//INSERT
        query = """INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    
    @classmethod
    def get_by_id(cls, data): #!READ
        query="SELECT * FROM users WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)

        if len(result) <1:
            return False
        return cls(result[0])
    

    @classmethod
    def get_by_email(cls, data): #!READ
        query="SELECT * FROM users WHERE email=%(email)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)

        if len(result) <1:
            return False
        return cls(result[0])

    #validate user
    @staticmethod #!VALIDATION
    def validate_user(data):
        is_valid = True

        if len(data['first_name'])<2:
            flash("First Name must be more than 2 characters!","register")
            is_valid = False
        if len(data['last_name'])<2:
            flash("Last Name must be more than 2 characters!","register")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Email must be valid !","register")
            is_valid = False
        elif User.get_by_email({'email':data['email']}):
            flash("Email already exist !","register")
            is_valid = False
        if len(data['password'])<6:
            flash("Password must be more than 6 characters!","register")
            is_valid = False
        elif data['password']!=data['confirm_password']:
            flash("Passwords do not match!","register")
            is_valid = False

        return is_valid
    