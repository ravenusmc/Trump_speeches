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

class Analysis():

    def start_analysis(self):
        textObject = Speeches()
        speech_text = textObject.get_speech_text()
        text_blog_text = textObject.get_speech_text_into_text_blog_version(speech_text)


test = Analysis()
test.start_analysis()
