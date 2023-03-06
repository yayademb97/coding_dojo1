from flask_app import app
from flask import render_template,request, redirect, session,flash
from flask_app.models.user_model import User
from flask_app.models.arbortrary_model import Arbortrary
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#* ***********Display Route***********
@app.route('/')
def log_reg():
    return render_template('index.html')

#* ***********Action Route***********
@app.route('/users/register', methods=['post'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')

    data={
        **request.form,
        'password':bcrypt.generate_password_hash(request.form['password'])
    }
    user=User.save_user(data)
    session['user_id']=user

    return redirect('/dashboard')


#* ***********Action Route***********
#Login user with validate form
@app.route('/users/login',methods=['POST'])
def login():
    user_db = User.get_by_email(request.form)
    if not user_db:
        flash('Invalid email or password',"login")
        return redirect('/')
    if not bcrypt.check_password_hash(user_db.password, request.form['password']):
        flash('Invalid email or password',"login")
        return redirect('/')
    session['user_id']=user_db.id
    return redirect('/dashboard')

#* ***********Display Route***********
@app.route('/dashboard')
def dash():
    if 'user_id' not in session:#?if he has not an id redirect to the register page
        return redirect('/')
    user = User.get_by_id({'id':session['user_id']})
    arbortraries=Arbortrary.get_all()
    return render_template('dashboard.html',user=user,all_arbortraries=arbortraries)