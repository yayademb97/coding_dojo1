from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.arbortrary_model import Arbortrary
from flask_app.models.user_model import User

#* ***********Display Route***********
@app.route('/new/tree')
def arbortrary_form():
    if 'user_id' not in session:#?if he has not an id redirect to the register page
        return redirect('/')
    user = User.get_by_id({'id':session['user_id']})
    return render_template('create_arbortrary.html',user=user)

#* ***********Action Route***********
@app.route('/arbortraries/create', methods=['post'])
def create_arbortrary():
    if not Arbortrary.validate_arbortrary(request.form):
        return redirect('/new/tree')
    trip_data={
        **request.form,
        'user_id': session['user_id']
    }
    Arbortrary.save_arbortrary(trip_data)
    return redirect('/dashboard')

#* ***********Display Route***********
@app.route('/arbortraries/detail/<int:arbortrary_id>')
def show_arbortrary(arbortrary_id):
    if 'user_id' not in session:#?if he has not an id redirect to the register page
        return redirect('/')
    arbortrary=Arbortrary.get_by_id_arbortrary({'id':arbortrary_id})
    user = User.get_by_id({'id':session['user_id']})
    # joined_people=User.people_joined_trip({'trip_id':trip_id})
    return render_template('show_arbortrary.html',arbortrary=arbortrary,user=user)

#* ***********Display Route***********
@app.route('/arortraries/edit/<int:arbortrary_id>')
def edit_arbortrary(arbortrary_id):
    if 'user_id' not in session:#?if he has not an id redirect to the register page
        return redirect('/')
    arbbortrary= Arbortrary.get_by_id_arbortrary({'id': arbortrary_id})
    # session['arbortrary_id']= arbortrary_id
    user = User.get_by_id({'id':session['user_id']})
    return render_template('edit_arbortrary.html',arbortrary=arbbortrary, user=user)

#* ***********Action Route***********
@app.route('/arbortraries/edit', methods=['post'])
def edit():
    if not Arbortrary.validate_arbortrary(request.form):
        id=session['arbortrary_id']
        return redirect(f'/arbortraries/edit/{id}')
    # arbortrary_data= {
    #     **request.form,
    #     'id': session['arbortrary_id']
    # }
    Arbortrary.update_arbortrary(request.form)
    return redirect('/dashboard')
@app.route('/user/account')
def my_trees():
    if 'user_id' not in session:#?if he has not an id redirect to the register page
        return redirect('/')
    user = User.get_by_id({'id':session['user_id']})
    arbortraries=Arbortrary.get_users_arbortrary({'user_id':session['user_id']})
    return render_template('user_account.html',user=user,all_arbortraries=arbortraries)

@app.route('/arbortraries/delete/<int:arbortrary_id>')
def delete(arbortrary_id):
    if 'user_id' not in session:#?if he has not an id redirect to the register page
        return redirect('/')
    
    Arbortrary.delete_arbortrary({'id':arbortrary_id})
    return redirect('/user/account')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


