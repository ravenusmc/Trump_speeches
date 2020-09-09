#This file will contain the code for the study

#importing supporting libraries
import numpy as np
import pandas as pd
import json
from textblob import TextBlob

#This class is what will be used to get all the speeches set up.
class Speeches():

    def __init__(self):
        self.first_speech = pd.read_json('./data/one.json', typ='series')
        self.second_speech = pd.read_json('./data/two.json', typ='series')
        self.third_speech = pd.read_json('./data/three.json', typ='series')
        self.fourth_speech = pd.read_json('./data/four.json', typ='series')
        self.fifth_speech = pd.read_json('./data/five.json', typ='series')
        self.sixth_speech = pd.read_json('./data/six.json', typ='series')
        self.seventh_speech = pd.read_json('./data/seven.json', typ='series')
        self.eigth_speech = pd.read_json('./data/eight.json', typ='series')
        self.ninth_speech = pd.read_json('./data/nine.json', typ='series')
        self.tenth_speech = pd.read_json('./data/ten.json', typ='series')
        self.eleventh_speech = pd.read_json('./data/eleven.json', typ='series')
        self.twelve_speech = pd.read_json('./data/twelve.json', typ='series')
        self.thirteen_speech = pd.read_json('./data/thirteen.json', typ='series')
        self.fourteen_speech = pd.read_json('./data/fourteen.json', typ='series')
        self.fifteen_speech = pd.read_json('./data/fifteen.json', typ='series')
        self.sixteen_speech = pd.read_json('./data/sixteen.json', typ='series')
        self.seventeen_speech = pd.read_json('./data/seventeen.json', typ='series')
        self.eightteen_speech = pd.read_json('./data/eightteen.json', typ='series')
        self.nineteen_speech = pd.read_json('./data/nineteen.json', typ='series')
        self.twenty_speech = pd.read_json('./data/twenty.json', typ='series')
        self.twenty_one_speech = pd.read_json('./data/twentyone.json', typ='series')
        self.all_speeches = [self.first_speech, self.second_speech, self.third_speech,
        self.fourth_speech, self.fifth_speech, self.sixth_speech, self.seventh_speech,
        self.eigth_speech, self.ninth_speech, self.tenth_speech, self.eleventh_speech,
        self.twelve_speech, self.thirteen_speech, self.fourteen_speech, self.fifteen_speech,
        self.sixteen_speech, self.seventeen_speech, self.eightteen_speech, self.nineteen_speech,
        self.twenty_speech, self.twenty_one_speech]

    def get_speech_text(self):
        speech_text = self.all_speeches[0]['text']
        return speech_text
        # total = 0
        # average_counter = 0
        # for sentence in text_ready_for_analysis.sentences:
        #     sentence_sentiment = sentence.sentiment[0]
        #     monthly_sentiment.append(sentence_sentiment)

    def get_speech_text_into_text_blog_version(self, speech_text):
        text_ready_for_analysis = TextBlob(speech_text)
        return text_ready_for_analysis




# test = Speeches()
# test.get_speech_text()
