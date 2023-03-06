from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__) 
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def playk():
    return 'hello'
   # Create a new instance of the Flask class called "app"
@app.route('/<int:x>/<int:y>/<color1>/<color2>')          # The "@" decorator associates this route with the function immediately following
def play_flask(x,y,color1, color2):
    return render_template("index.html",x=x,y=y,color1=color1,color2=color2)  # Return the string 'Play!' as a response


# import statements, maybe some other routes

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
