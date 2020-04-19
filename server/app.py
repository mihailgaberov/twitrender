from flask import Flask, jsonify, request
from flask_cors import CORS
from db import DB

db = DB()

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
def test():
    return jsonify('Miki rulzzz...')
app.add_url_rule('/', 'test', test)

# Search for a given word
@app.route('/search/<word>', methods=['GET'])
def search(word):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        result = db.search(word.strip())
    return jsonify(result)


if __name__ == '__main__':
    app.run()
