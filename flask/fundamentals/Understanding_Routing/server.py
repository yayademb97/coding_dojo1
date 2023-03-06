from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"




@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!' # Return the string 'Hello World!' as a response


# import statements, maybe some other routes
    
@app.route('/dojo')
def success():
    return 'dojo!'     # app.run(debug=True) should be the very last statement! 


@app.route('/say/<name>')
def say_hi(name):
    return f" hi {name}"

@app.route('/repeat/<time>/<name>')
def yaya(name,time):
    return f" <h1>{name}</h1><br>"  * int(time)










if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

