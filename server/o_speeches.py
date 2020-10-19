#This file will contain the code for the study

#importing supporting libraries
import numpy as np
import pandas as pd
import json
# import os
# print(os.getcwd())

#This class is what will be used to get all the speeches set up.
class obama_speeches():

    def __init__(self):
        self.first_speech = pd.read_json('./data/o_speech_one.json', typ='series')
        self.second_speech = pd.read_json('./data/o_speech_two.json', typ='series')
        self.third_speech = pd.read_json('./data/o_speech_three.json', typ='series')
        self.fourth_speech = pd.read_json('./data/o_speech_four.json', typ='series')
        self.fifth_speech = pd.read_json('./data/o_speech_five.json', typ='series')
        self.sixth_speech = pd.read_json('./data/o_speech_six.json', typ='series')
        self.seventh_speech = pd.read_json('./data/o_speech_seven.json', typ='series')
        self.eigth_speech = pd.read_json('./data/o_speech_eight.json', typ='series')
        self.ninth_speech = pd.read_json('./data/o_speech_nine.json', typ='series')
        self.tenth_speech = pd.read_json('./data/o_speech_ten.json', typ='series')
        self.all_speeches = [self.first_speech, self.second_speech, self.third_speech,
        self.fourth_speech, self.fifth_speech, self.sixth_speech, self.seventh_speech,
        self.eigth_speech, self.ninth_speech, self.tenth_speech]

#     def test_working(self):
#         print(self.tenth_speech)
#
#
# test = Obama()
# test.test_working()
