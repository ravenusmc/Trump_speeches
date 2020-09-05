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
        #pass
        self.first_speech = pd.read_json('./data/one.json', typ='series')
        self.second_speech = pd.read_json('./data/two.json', typ='series')
        self.sixth_speech = pd.read_json('./data/six.json', typ='series')
        self.ninth_speech = pd.read_json('./data/nine.json', typ='series')
        #self.speeches = pd.read_json("./data/test.json", lines = True)

    def working(self):
        # data = json.load(open('./data/trumpspeeches.json'))
        # print(type(data))
        print(self.ninth_speech['speechlocation'])
        # with Path("./data/test.json").open("r") as f:
        #     for line in f:
        #         try:
        #             json.loads(f)
        #         except:
        #             print("Problem:", line)



test = textAnalysis()
test.working()
