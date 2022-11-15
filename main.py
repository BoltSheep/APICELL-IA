from flask import Flask
app = Flask(__name__)

@app.route('/')

def statusCheck():
    return"500"