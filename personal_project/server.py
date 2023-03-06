from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__) 


@app.route('/')  # The "@" decorator associates this route with the function immediately following
def main():
    return 'Welcome'