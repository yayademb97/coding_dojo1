from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user

class Student:
    def __init__(self,data):
        self.id=data['id']
        self.class_name=data['class_name']
        self.on_line=data['on_line']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        self.owner = user.User.get_by_id({'id':self.user_id})
    
    
    @classmethod
    def save_student(cls, data): #!CREATE
        query="INSERT INTO students (user_id,class_name) VALUES (%(user_id)s,%(class_name)s);"
        # this query will return the id of the new student insert
        return connectToMySQL(DATABASE).query_db(query,data)
    

    #get all students
    @classmethod  #read 
    def get_students(cls): #!READ
        query="SELECT * FROM students;" 
        results= connectToMySQL(DATABASE).query_db(query)
        #organize the results
        students=[]
        for row in results:
            students.append(cls(row))
        return students
    
    #get one recipe by id
    @classmethod
    def get_by_id_student(cls,data): #!READ
        query="SELECT * FROM students WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])
    
    @classmethod
    def update_student(cls,data): #!UPDATE//EDIT
        query="""UPDATE students SET class_name=%(class_name)s,
                on_line=%(on_line)s 
                WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete_student(cls,data): #!DELETE
        query="DELETE FROM students WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    #validate student 
    @staticmethod #!VALIDATION
    def validate_student(data): 
        is_valid = True

        if len(data['class_name'])<3:
            flash("Name must be more than 3 characters!","student")
            is_valid = False
        # if len(data['email'])<3:
        #     flash("On Line must not be blank!","student")
            # is_valid = False
            
        return is_valid
    
    
