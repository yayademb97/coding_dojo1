from flask_app import app
from flask import render_template,request, redirect, session,flash
from flask_app.models.user import User
from flask_app.models.student import Student
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/students/new')
def student_form():
    if 'user_id' not in session:#if he has not an id redirect to the register page
        return redirect('/')
    return render_template('create_student.html')

@app.route('/students/create', methods=['post'])
def create_student():
    if not Student.validate_student(request.form):
        return redirect('/students/new')
    student_data={
        **request.form,
        'user_id': session['user_id']
    }
    Student.save_student(student_data)
    return redirect('/students')
@app.route('/students/show/<int:student_id>')
def show_student(student_id):
    if 'user_id' not in session:#if he has not an id redirect to the register page
        return redirect('/')
    student=Student.get_by_id_student({'id':student_id})
    user = User.get_by_id({'id':session['user_id']})
    return render_template('show_student.html',student=student,user=user)

@app.route('/students/edit/<int:student_id>')
def edit_student(student_id):
    if 'user_id' not in session:#if he has not an id redirect to the register page
        return redirect('/')
    student= student.get_by_id_student({'id': student_id})
    session['student_id']= student_id
    return render_template('edit_student.html',student=student)

@app.route('/students/edit', methods=['post'])
def edit():
    if not Student.validate_student(request.form):
        return redirect(f'/students/edit/{id}')#checkeeeer
    student_data= {
        **request.form,
        'id': session['student_id']
    }
    Student.update_student(student_data)
    return redirect('/students')


@app.route('/students/delete/<int:student_id>')
def delete(student_id):
    Student.delete_student({'id':student_id})
    return redirect('/students')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
