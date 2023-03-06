from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__) 

   # Create a new instance of the Flask class called "app"
@app.route('/<int:x>/<color>')          # The "@" decorator associates this route with the function immediately following
def play_flask(x,color):
    return render_template("index.html",x=x,color=color)  # Return the string 'Play!' as a response


# import statements, maybe some other routes

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
