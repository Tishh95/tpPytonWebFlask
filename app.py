from flask import Flask, render_template, jsonify
import json ,os
app = Flask(__name__)



books = json.load(open("Data/books.json"))

@app.route("/")
def index():
 return print("/api/books   /api/book/<id>   api/bookT/<title> ")

@app.route("/api/books", methods=["GET"])
def get_books():
        return render_template('input.html', data=books)

@app.route("/api/book/<id>", methods=['GET'])
def getById(id):
	for b in books:
		if b.get('isbn') == (id):
			return render_template('book.html', data =b)
		else:
			pass

@app.route("/api/bookT/<title>", methods=['GET'])
def getByTitle(title):
	for b in books:
		if b.get('title') == title:
			return render_template('book.html', data =b)
		else:
			pass

app.run(debug=True , host='0.0.0.0', port=5000)

