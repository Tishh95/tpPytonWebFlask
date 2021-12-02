import streamlit  as st, pandas as pd , seaborn as sns , numpy as pd , json , os
from flask import Flask ,request, render_template
app = Flask(__name__)



SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT,  "books.json")
data = json.load(open(json_url))
jsonStr = json.dumps(data)

@app.route("/")
def index():
 return render_template('book.html' , name="name")

@app.route("/api/books", methods=['GET'])
def hello():
    jsonStr = json.dumps(data)
    return jsonStr

@app.route("/api/book/<id>", methods=['GET'])
def getById(id):
	for b in data:
		if b.get('isbn') == (id):
			return render_template('book.html', data =b)
		else:
			pass

@app.route("/api/bookT/<title>", methods=['GET'])
def getByTitle(title):
	for b in data:
		if b.get('title') == title:
			return render_template('book.html', data =b)
		else:
			pass
app.run(debug=True)

