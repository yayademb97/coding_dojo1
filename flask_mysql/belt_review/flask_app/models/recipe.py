from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user

class Recipe:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.date_made=data['date_made']
        self.under_30=data['under_30']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        self.owner = user.User.get_by_id({'id':self.user_id})


    @classmethod
    def save_recipe(cls, data): #!CREATE
        query="INSERT INTO recipes (user_id,name,description,instructions,date_made,under_30) VALUES (%(user_id)s,%(name)s,%(description)s,%(instructions)s,%(date_made)s,%(under_30)s);"
        # this query will return the id of the new recipe insert
        return connectToMySQL(DATABASE).query_db(query,data)
    

    #get all recipes
    @classmethod  #read 
    def get_recipes(cls): #!READ
        query="SELECT * FROM recipes;" 
        results= connectToMySQL(DATABASE).query_db(query)
        #organize the results
        recipes=[]
        for row in results:
            recipes.append(cls(row))
        return recipes
    
    #get one recipe by id
    @classmethod
    def get_by_id_recipe(cls,data): #!READ
        query="SELECT * FROM recipes WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])
    
    @classmethod
    def update_recipe(cls,data): #!UPDATE//EDIT
        query="""UPDATE recipes SET name=%(name)s,
                description=%(description)s,instructions=%(instructions)s,date_made=%(date_made)s,under_30=%(under_30)s 
                WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete_recipe(cls,data): #!DELETE
        query="DELETE FROM recipes WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    #validate recipe 
    @staticmethod #!VALIDATION
    def validate_recipe(data): 
        is_valid = True

        if len(data['name'])<3:
            flash("Name must be more than 3 characters!","recipe")
            is_valid = False
        if len(data['description'])<3:
            flash("Description must not be blank!","recipe")
            is_valid = False
        if len(data['instructions'])<3:
            flash("Instructions must be more than 3 characters!","recipe")
            is_valid=False
        if data['date_made']=="":
            flash("Made Date must be not blank!","recipe")
            is_valid = False
            
        return is_valid
    
    
