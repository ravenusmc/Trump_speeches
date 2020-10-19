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
from o_speeches import *

class Analysis():

    def __init__(self):
        self.textObject = Speeches()
        self.examine = Examine()
        self.support = Support()
        self.o_speeches = obama_speeches()

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
        return format(mean, '.2f')

    def get_sentence_from_speech(self, speech_title, position):
        # I have to find the spefic speech that holds the title that the user wants.
        speech_JSON = self.examine.find_specific_speech(self.textObject, speech_title)
        # Getting the actual speech out of the JSON.
        speech_text = self.examine.get_speech_text(speech_JSON)
        speech_in_list = self.support.turn_speech_string_to_list(speech_text)
        return speech_in_list[position]

    def get_speech_length(self, speech_title):
        # I have to find the spefic speech that holds the title that the user wants.
        speech_JSON = self.examine.find_specific_speech(self.textObject, speech_title)
        # Getting the actual speech out of the JSON.
        speech_text = self.examine.get_speech_text(speech_JSON)
        speech_in_list = self.support.turn_speech_string_to_list(speech_text)
        return len(speech_in_list)

    def get_sentiment_by_sentence_by_speech(self, speech_title, position):
        # I have to find the spefic speech that holds the title that the user wants.
        speech_JSON = self.examine.find_specific_speech(self.textObject, speech_title)
        # Getting the actual speech out of the JSON.
        speech_text = self.examine.get_speech_text(speech_JSON)
        speech_in_list = self.support.turn_speech_string_to_list(speech_text)
        sentence = speech_in_list[position]
        sentence_sentiment = format(self.examine.get_sentiment_of_sentence(sentence), '.2f')
        # Making a list to hold the sentence and sentiment to send back to the client side
        sentence_and_sentiment_list = []
        sentence_and_sentiment_list.append(sentence)
        sentence_and_sentiment_list.append(sentence_sentiment)
        return sentence_and_sentiment_list

    def sentiment_of_all_speeches(self):
        # Use self.o_speeches for Obama speeches, self.textObject for Trump speeches
        sentiment_collection = self.examine.get_sentiment_by_all_speeches(self.o_speeches)
        print(sentiment_collection)


    def get_most_common_words_by_speech(self, speech_title):
        speech_JSON = self.examine.find_specific_speech(self.textObject, speech_title)
        speech_text = self.examine.get_speech_text(speech_JSON)
        words_in_list = self.examine.build_speech_into_list(speech_text)
        word_and_count = self.support.clean_word_list(words_in_list)
        word_and_count_chart_data = self.examine.build_chart_data_word_and_count(word_and_count)
        return word_and_count_chart_data

speech_title = 'Remarks by President Trump at Tax Reform Event'
position = 0
test = Analysis()
test.sentiment_of_all_speeches()

# test.get_sentence_from_speech(speech_title, position)
#Remarks at a Make America Great Again Rally in Melbourne Florida => eightteen.json

# Getting the length of the speech in the list
# length_of_speech_in_list = len(speech_in_list)
