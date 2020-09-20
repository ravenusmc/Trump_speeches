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
from support import *

class Analysis():

    def __init__(self):
        self.textObject = Speeches()
        self.examine = Examine()
        self.support = Support()

    def start_analysis(self):
        speech_text = self.examine.get_speech_text(self.textObject)
        text_blog_text = self.examine.get_speech_text_into_text_blog_version(speech_text)

    def get_sentiment_by_speech(self, speech_title):
        # I have to find the spefic speech that holds the title that the user wants.
        speech_JSON = self.examine.find_specific_speech(self.textObject, speech_title)
        # Getting the actual speech out of the JSON.
        speech_text = self.examine.get_speech_text(speech_JSON)
        # Getting the speech into the textblog version
        speech_textblob_version = self.examine.get_speech_text_into_textblob_version(speech_text)
        # Getting the sentiment of each line and storing it in a list
        sentiment_list = self.examine.build_sentiment_list(speech_textblob_version)
        # Getting the mean sentiment from the list
        mean = self.examine.get_average_from_list(sentiment_list)
        return mean

    def get_sentiment_by_sentence_by_speech(self, speech_title, position):
        # I have to find the spefic speech that holds the title that the user wants.
        speech_JSON = self.examine.find_specific_speech(self.textObject, speech_title)
        # Getting the actual speech out of the JSON.
        speech_text = self.examine.get_speech_text(speech_JSON)
        speech_in_list = self.support.turn_speech_string_to_list(speech_text)
        sentence = speech_in_list[position]
        sentence_sentiment = self.examine.get_sentiment_of_sentence(sentence)
        # Making a list to hold the sentence and sentiment to send back to the client side
        sentence_and_sentiment_list = []
        sentence_and_sentiment_list.append(sentence)
        sentence_and_sentiment_list.append(sentence_sentiment)
        return sentence_and_sentiment_list

    def sentiment_of_all_speeches(self):
        sentiment_collection = self.examine.get_sentiment_by_all_speeches(self.textObject)

    def get_most_common_words_by_speech(self, speech_title):
        speech_JSON = self.examine.find_specific_speech(self.textObject, speech_title)
        speech_text = self.examine.get_speech_text(speech_JSON)
        print(speech_text)
        # Once I have the text object I have to loop through the speech
        # getting the most common words

        pass

test = Analysis()
#test.start_analysis()
speech_title = 'Remarks at a Make America Great Again Rally in Melbourne Florida'
position = 10
test.get_most_common_words_by_speech(speech_title)
#Remarks at a Make America Great Again Rally in Melbourne Florida => eightteen.json

# Getting the length of the speech in the list
# length_of_speech_in_list = len(speech_in_list)
