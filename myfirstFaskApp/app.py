from flask import Flask
import json

app = Flask(__name__)

with open('./books.json') as f:
  database = json.load(f)

@app.route('/', methods=['GET'])
def home():
    return "Hello home page", 200

@app.route('/api/books', methods=['GET'])
def books():
    return json.dumps(database), 200

@app.route('/api/books/<int:isbn>', methods=['GET'])
def searchByIsbn(isbn):
  for book in database:
    if book['isbn'] == isbn:
      return json.dumps(book), 200
  return "Le livre est introuvable !", 404

@app.route('/api/books/<string:title>', methods=['GET'])
def searchByTitle(title):
  for book in database:
    if book['title'] == title:
      return json.dumps(book), 200
  return "Le livre est introuvable !", 404

if __name__ == '__main__':
  app.run(debug=True)