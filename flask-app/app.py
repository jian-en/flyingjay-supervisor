import flask

app = flask.Flask(__name__)

@app.route('/json')
def json():
    return flask.jsonify(message='Hello, World!')
