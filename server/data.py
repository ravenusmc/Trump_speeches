#This file will contain the code to actually do text analysis

#importing supporting libraries
import numpy as np
import pandas as pd
import json
import datetime
from textblob import TextBlob
from pathlib import Path

#Importing files I built
from speeches import *
from examine import *

class Analysis():

    def start_analysis(self):
        textObject = Speeches()
        examine = Examine()
        speech_text = examine.get_speech_text(textObject)
        text_blog_text = examine.get_speech_text_into_text_blog_version(speech_text)
        print(text_blog_text)

    def get_sentiment_by_speech(self):
        pass


test = Analysis()
test.start_analysis()
