# This class is what will examine the speeches

# importing supporting libraries
import numpy as np
import pandas as pd
import json
from textblob import TextBlob

# Importing libraries I made
from support import *

# This class is what will be used to examine the speeches using text blob.
class Examine():

    def get_speech_text(self, textObject):
        speech_text = textObject.all_speeches[0]['text']
        return speech_text
        # total = 0
        # average_counter = 0
        # for sentence in text_ready_for_analysis.sentences:
        #     sentence_sentiment = sentence.sentiment[0]
        #     monthly_sentiment.append(sentence_sentiment)

    def find_specific_speech(self, textObject, speech_title):
        support = Support()
        #looping through the textObject to find the speech I need
        speech_JSON = support.loop_to_find_speech(textObject, speech_title)
        print(speech_JSON)

    def get_speech_text_into_textblob_version(self, speech_text):
        text_ready_for_analysis = TextBlob(speech_text)
        return text_ready_for_analysis
