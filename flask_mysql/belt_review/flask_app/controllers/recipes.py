from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipes/new')
def recipe_form():
    if 'user_id' not in session:#if he has not an id redirect to the register page
        return redirect('/')
    return render_template('create_recipe.html')

@app.route('/recipes/create', methods=['post'])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    recipe_data={
        **request.form,
        'user_id': session['user_id']
    }
    Recipe.save_recipe(recipe_data)
    return redirect('/recipes')


@app.route('/recipes/show/<int:recipe_id>')
def show_recipe(recipe_id):
    if 'user_id' not in session:#if he has not an id redirect to the register page
        return redirect('/')
    recipe=Recipe.get_by_id_recipe({'id':recipe_id})
    user = User.get_by_id({'id':session['user_id']})
    return render_template('show_recipe.html',recipe=recipe,user=user)

@app.route('/recipes/edit/<int:recipe_id>')
def edit_recipe(recipe_id):
    if 'user_id' not in session:#if he has not an id redirect to the register page
        return redirect('/')
    recipe= Recipe.get_by_id_recipe({'id': recipe_id})
    session['recipe_id']= recipe_id
    return render_template('edit_recipe.html',recipe=recipe)

@app.route('/recipes/edit', methods=['post'])
def edit():
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/edit/{id}')#checkeeeer
    recipe_data= {
        **request.form,
        'id': session['recipe_id']
    }
    Recipe.update_recipe(recipe_data)
    return redirect('/recipes')


@app.route('/recipes/delete/<int:recipe_id>')
def delete(recipe_id):
    Recipe.delete_recipe({'id':recipe_id})
    return redirect('/recipes')



