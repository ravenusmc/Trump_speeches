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

    def find_specific_speech(self, textObject, speech_title):
        support = Support()
        #looping through the textObject to find the speech I need
        speech_JSON = support.loop_to_find_speech(textObject, speech_title)
        return speech_JSON

    def get_speech_text(self, speech_JSON):
        speech_text = speech_JSON['text']
        return speech_text

    def get_speech_text_into_textblob_version(self, speech_text):
        speech_textblob_version = TextBlob(speech_text)
        return speech_textblob_version

    def build_sentiment_list(self, speech_textblob_version):
        sentiment_sentence_list = []
        for sentence in speech_textblob_version.sentences:
            sentence_sentiment = sentence.sentiment[0]
            sentiment_sentence_list.append(sentence_sentiment)
        return sentiment_sentence_list

    def get_average_from_list(self, sentiment_list):
        return sum(sentiment_list) / len(sentiment_list)

    def get_sentiment_of_sentence(self, sentence):
        sentence_ready_for_analysis = TextBlob(sentence)
        sentence_sentiment = sentence_ready_for_analysis.sentiment[0]
        return sentence_sentiment
