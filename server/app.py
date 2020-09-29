from flask import Flask, jsonify, request
from flask_cors import CORS

#importing code that I wrote
# from data import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)
# CORS(app, resources={r'/*': {'origins': '*'}})

# This route will get the data for the first chart.
@app.route('/single_speech_chart', methods=['GET', 'POST'])
def single_speech_chart():
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
