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

    def start_analysis(self):
        textObject = Speeches()
        examine = Examine()
        speech_text = examine.get_speech_text(textObject)
        text_blog_text = examine.get_speech_text_into_text_blog_version(speech_text)

    def get_sentiment_by_speech(self, speech_title):
        textObject = Speeches()
        examine = Examine()
        # I have to find the spefic speech that holds the title that the user wants.
        speech_JSON = examine.find_specific_speech(textObject, speech_title)
        # Getting the actual speech out of the JSON.
        speech_text = examine.get_speech_text(speech_JSON)
        # Getting the speech into the textblog version
        speech_textblob_version = examine.get_speech_text_into_textblob_version(speech_text)
        # Getting the sentiment of each line and storing it in a list
        sentiment_list = examine.build_sentiment_list(speech_textblob_version)
        # Getting the mean sentiment from the list
        mean = examine.get_average_from_list(sentiment_list)
        return mean

    def get_sentiment_by_sentence_by_speech(self, speech_title, position):
        textObject = Speeches()
        examine = Examine()
        support = Support()
        # I have to find the spefic speech that holds the title that the user wants.
        speech_JSON = examine.find_specific_speech(textObject, speech_title)
        # Getting the actual speech out of the JSON.
        speech_text = examine.get_speech_text(speech_JSON)
        speech_in_list = support.turn_speech_string_to_list(speech_text)
        sentence = speech_in_list[position]
        sentence_sentiment = examine.get_sentiment_of_sentence(sentence)
        # Making a list to hold the sentence and sentiment to send back to the client side
        sentence_and_sentiment_list = []
        sentence_and_sentiment_list.append(sentence)
        sentence_and_sentiment_list.append(sentence_sentiment)
        return sentence_and_sentiment_list


    def sentiment_of_all_speeches(self):
        pass

test = Analysis()
#test.start_analysis()
speech_title = 'Remarks at a Make America Great Again Rally in Melbourne Florida'
position = 10
test.get_sentiment_by_sentence_by_speech(speech_title, position)
#Remarks at a Make America Great Again Rally in Melbourne Florida => eightteen.json

# Getting the length of the speech in the list
# length_of_speech_in_list = len(speech_in_list)
