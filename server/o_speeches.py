#This file will contain the code for the study

#importing supporting libraries
import numpy as np
import pandas as pd
import json
# from textblob import TextBlob

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
        self.all_speeches = [self.first_speech, self.second_speech, self.third_speech,
        self.fourth_speech, self.fifth_speech, self.sixth_speech, self.seventh_speech,
        self.eigth_speech, self.ninth_speech, self.tenth_speech, self.eleventh_speech,
        self.twelve_speech, self.thirteen_speech, self.fourteen_speech, self.fifteen_speech,
        self.sixteen_speech, self.seventeen_speech, self.eightteen_speech, self.nineteen_speech,
        self.twenty_speech, self.twenty_one_speech]
