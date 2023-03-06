from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Phone:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.model=data['model']
        self.order_now=data['order_now']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        self.owner = user_model.User.get_by_id({'id':self.user_id})

    @classmethod
    def save_phone(cls, data): #!CREATE
        query="INSERT INTO phones (user_id,name,description,model,order_now) VALUES (%(user_id)s,%(name)s,%(description)s,%(model)s,%(order_now)s);"
        # this query will return the id of the new phone insert
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #get all phones
    @classmethod  #read 
    def get_phones(cls): #!READ
        query="SELECT * FROM phones;" 
        results= connectToMySQL(DATABASE).query_db(query)
        #organize the results
        phones=[]
        for row in results:
            phones.append(cls(row))
        return phones
    
    #get one phone by id
    @classmethod
    def get_by_id_phone(cls,data): #!READ
        query="SELECT * FROM phones WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

    @classmethod
    def update_phone(cls,data): #!UPDATE//EDIT
        query="""UPDATE phones SET name=%(name)s,
                description=%(description)s,model=%(model)s,order_now=%(order_now)s 
                WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete_phone(cls,data): #!DELETE
        query="DELETE FROM phones WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    #validate phone 
    @staticmethod #!VALIDATION
    def validate_phone(data): 
        is_valid = True

        if len(data['name'])<3:
            flash("Name must be more than 3 characters!","phone")
            is_valid = False
        if len(data['description'])<3:
            flash("Description must not be blank!","phone")
            is_valid = False
        if len(data['model'])<3:
            flash("Model must be more than 3 characters!","phone")
            is_valid=False
            
        return is_valid
    

