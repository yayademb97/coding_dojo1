from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
# from datetime import datetime

class Arbortrary:
    def __init__(self,data):
        self.id=data['id']
        self.species=data['species']
        self.location=data['location']
        self.reason=data['reason']
        self.date_planted=data['date_planted']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        self.creator = user_model.User.get_by_id({'id':self.user_id})

    
    #* ***********CREATE ARBORTRARY***********
    @classmethod
    def save_arbortrary(cls, data): #!CREATE
        query="INSERT INTO abortraries (user_id,species,location,reason,date_planted) VALUES (%(user_id)s,%(species)s,%(location)s,%(reason)s,%(date_planted)s);"
        
        # this query will return the id of the new arbortrary insert
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #* ***********GET ALL USERS ARBORTRARIES WITH DETAILS***********
    #get all arbortraries
    @classmethod 
    def get_users_arbortrary(cls, data): #!READ
        query="""SELECT * FROM abortraries
                WHERE user_id = %(user_id)s 
                ORDER BY abortraries.created_at DESC;
                """ 
        results= connectToMySQL(DATABASE).query_db(query, data)
        #organize the results
        arbortraries=[]
        for row in results:
            arbortraries.append(cls(row))
        return arbortraries
    @classmethod 
    def get_all(cls): #!READ
        query="""SELECT * FROM abortraries;
                """ 
        results= connectToMySQL(DATABASE).query_db(query)
        #organize the results
        arbortraries=[]
        for row in results:
            arbortraries.append(cls(row))
        return arbortraries
    
     #* ***********GET ONE ARBORTRARY BY ID***********
    #get one arbortrary by id
    @classmethod
    def get_by_id_arbortrary(cls,data): #!READ
        query="SELECT * FROM abortraries WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])
    
     #* ***********UPDATE ARBORTRARY***********
    @classmethod
    def update_arbortrary(cls,data): #!UPDATE//EDIT
        query="""UPDATE abortraries 
                SET species=%(species)s,location=%(location)s,reason=%(reason)s,date_planted=%(date_planted)s
                WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #* ***********DELETE ARBORTRARY***********
    @classmethod
    def delete_arbortrary(cls,data): #!DELETE
        query="DELETE FROM abortraries WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
     #* ***********VALIDATE ARBORTRARY*********** 
    @staticmethod #!VALIDATION
    def validate_arbortrary(data): 
        is_valid = True

        if len(data['species'])<5:
            flash("species must be more than 5 characters!","arbortrary")
            is_valid = False
        
        if len(data['location'])<2:
            flash("location must be more than 2 characters!","arbortrary")
            is_valid = False
        
        if len(data['reason'])>50:
            flash("reason must be less than 50 characters!","arbortrary")
            is_valid = False
        
        return is_valid
