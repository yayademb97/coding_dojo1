from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__) 
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/')
def success():
    return "success"
@app.route('/hello/<string:banana>/<int:num>')
def hello():
    return render_template("hello.html, banana=banana, num=num")
            
@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student = [
    {'name' : 'Michael', 'age' : 35},
    {'name' : 'John', 'age' : 30 },
    {'name' : 'Mark', 'age' : 25},
    {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], student = student)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5008)    # Run the app in debug mode.
