from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.phone_model import Phone
from flask_app.models.user_model import User

@app.route('/phones/new')
def phone_form():
    if 'user_id' not in session:#if he has not an id redirect to the register page
        return redirect('/')
    return render_template('create_phone.html')

@app.route('/phones/create', methods=['post'])
def create_phone():
    if not Phone.validate_phone(request.form):
        return redirect('/phones/new')
    phone_data={
        **request.form,
        'user_id': session['user_id']
    }
    Phone.save_phone(phone_data)
    return redirect('/phones')

@app.route('/phones/show/<int:phone_id>')
def show_phone(phone_id):
    if 'user_id' not in session:#if he has not an id redirect to the register page
        return redirect('/')
    phone=Phone.get_by_id_phone({'id':phone_id})
    user = User.get_by_id({'id':session['user_id']})
    return render_template('show_phone.html',phone=phone,user=user)

@app.route('/phones/edit/<int:phone_id>')
def edit_phone(phone_id):
    if 'user_id' not in session:#if he has not an id redirect to the register page
        return redirect('/')
    phone= Phone.get_by_id_phone({'id': phone_id})
    session['phone_id']= phone_id
    return render_template('edit_phonee.html',phone=phone)

@app.route('/phones/edit', methods=['post'])
def edit():
    phone_data= {
        **request.form,
        'id': session['phone_id']
    }
    Phone.update_phone(phone_data)
    return redirect('/phones')

@app.route('/phones/delete/<int:phone_id>')
def delete(phone_id):
    Phone.delete_phone({'id':phone_id})
    return redirect('/phones')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')