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
        speech_length = speech_object.get_speech_length(speech)
        print(speech_length)
        speech_data = []
        speech_data.append(speech_mean)
        speech_data.append(speech_length)
    return jsonify(speech_data)

# This route will get the data for the sentiment by sentence.
@app.route('/fetch_speech_sentence_sentiment', methods=['GET', 'POST'])
def fetchSpeechSentenceSentiment():
    if request.method == 'POST':
        speech_object = Analysis()
        post_data = request.get_json()
        speech_title = post_data['speech']
        position = post_data['value']
        sentence_and_sentiment_list = speech_object.get_sentiment_by_sentence_by_speech(speech_title, position)
    return jsonify(sentence_and_sentiment_list)

# This route will get the data for the sentiment by sentence.
@app.route('/fetch_word_count', methods=['GET', 'POST'])
def fetch_word_count():
    if request.method == 'POST':
        speech_object = Analysis()
        post_data = request.get_json()
        speech_title = post_data['speech']
        word_and_count_chart_data = speech_object.get_most_common_words_by_speech(speech_title)
        print(word_and_count_chart_data)
    return jsonify(word_and_count_chart_data)


if __name__ == '__main__':
    app.run()
