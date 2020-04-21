from flask import Flask, jsonify, request
from flask_cors import CORS
from db import DB
from markupsafe import escape

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
    if request.method == 'GET':
        start_date = request.args.get('start_date', None)
        end_date = request.args.get('end_date', None)
        result = db.search(escape(word.strip()), escape(start_date), escape(end_date))
    return jsonify(result)


if __name__ == '__main__':
    app.run()
