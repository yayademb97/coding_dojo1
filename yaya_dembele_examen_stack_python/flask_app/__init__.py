from flask import Flask
app = Flask(__name__)
app.secret_key = "black belt key"
DATABASE = "abortrary_schemas"