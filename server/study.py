#This file will contain the code for the study

#importing supporting libraries
import numpy as np
import pandas as pd
import json
import datetime
from textblob import TextBlob
from pathlib import Path

#This class is what will be used to do the data analysis.
class textAnalysis():

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

    def working(self):
        # data = json.load(open('./data/trumpspeeches.json'))
        # print(type(data))
        print(self.second_speech['speechlocation'])
        # with Path("./data/test.json").open("r") as f:
        #     for line in f:
        #         try:
        #             json.loads(f)
        #         except:
        #             print("Problem:", line)



test = textAnalysis()
test.working()
