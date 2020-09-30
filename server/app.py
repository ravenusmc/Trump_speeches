from flask import Flask, jsonify, request
from flask_cors import CORS

#importing code that I wrote
from data import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)
# CORS(app, resources={r'/*': {'origins': '*'}})

# This route will get the data for the first chart.
@app.route('/get_sentiment_by_speech', methods=['GET', 'POST'])
def get_sentiment_by_speech():
    if request.method == 'POST':
        speech_object = Analysis()
        post_data = request.get_json()
        speech = post_data['speech']
        speech_mean = speech_object.get_sentiment_by_speech(speech)
    return jsonify(speech_mean)


if __name__ == '__main__':
    app.run()
