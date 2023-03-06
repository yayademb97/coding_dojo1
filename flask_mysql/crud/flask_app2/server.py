from flask import Flask, render_template, request, redirect,session
# import the class from users.py
from users import User
app = Flask(__name__)
app.secret_key='shhhhhhhhhh oussama'
@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html", users=users)


@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the User class.
    user_id=User.save(data)
    session['id']=user_id
    # Don't forget to redirect after saving to the database.
    return redirect('/show')  
@app.route('/show')
def show():
    print('--------------------------------')
    #print(session['id'])

    users= User.get_by_id({'id':session['id']})
    return render_template("create_new_user.html", users=users)









if __name__ == "__main__":
    app.run(debug=True, port="5012")