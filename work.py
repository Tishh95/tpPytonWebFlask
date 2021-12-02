import streamlit  as st, pandas as pd , seaborn as sns , numpy as pd
from flask import Flask ,request

app = Flask(__name__)

@app.route("/")
def index():
 return "title"
    

@app.route('/hello')
def hello():
    return 'Hello, World '

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % (username)


@app.route('/login', methods=['GET', 'POST'])
def login():
        return "post"


app.run(debug=True)

