from flask_app import app, render_template

@app.route("/")
def regist_log():

    return render_template("log_reg.html")


    #==========Action ROute=============
@app.route("/users/create", methods=["post"])
def register():
    print(request.form)
    return redirect("/")
    User.create(request.form)
    return redirect("/dashboard")
    #==========Display Route=============
    @app.route("/dashboard")
    def 