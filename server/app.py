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

# This route will get the data for the sentiment by sentence.
@app.route('/fetch_speech_sentence_sentiment', methods=['GET', 'POST'])
def fetchSpeechSentenceSentiment():
    if request.method == 'POST':
        speech_object = Analysis()
        post_data = request.get_json()
        speech_title = post_data['speech']
        position = post_data['value']
        # speech = post_data['speech']
        #speech_mean = speech_object.get_sentiment_by_sentence_by_speech(speech_title, position)
    return jsonify('HI')


if __name__ == '__main__':
    app.run()
