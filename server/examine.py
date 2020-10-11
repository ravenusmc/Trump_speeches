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

    def get_sentiment_by_all_speeches(self, textObject):
        count = 0
        sentiment_collection = []
        columns = ['Speech_Title', 'Sentiment']
        sentiment_collection.append(columns)
        # I need to get the speech title and sentiment of each speech
        while count < len(textObject.all_speeches):
            rows = []
            speech_title = textObject.all_speeches[count]['speechtitle']
            speech_text = textObject.all_speeches[count]['text']
            speech_textblob_version = self.get_speech_text_into_textblob_version(speech_text)
            sentiment_sentence_list = self.build_sentiment_list(speech_textblob_version)
            sentiment_mean_by_speech = self.get_average_from_list(sentiment_sentence_list)
            rows.append(speech_title)
            rows.append(sentiment_mean_by_speech)
            sentiment_collection.append(rows)
            count += 1
        return sentiment_collection

    def build_speech_into_list(self, speech_text):
        return list(speech_text.split(" "))

    def build_chart_data_word_and_count(self, word_and_count):
        word_and_count_chart_data = []
        columns = ['Word', 'Count']
        word_and_count_chart_data.append(columns)
        for word, count in word_and_count.items():
            rows = []
            rows.append(word)
            rows.append(count)
            word_and_count_chart_data.append(rows)
        return word_and_count_chart_data
