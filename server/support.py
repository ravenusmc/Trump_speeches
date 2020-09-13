# This class will focus on providing methods that support the rest of
# the application.

class Support():

    def loop_to_find_speech(self, textObject, speech_title):
        count = 0
        while count < len(textObject.all_speeches):
            if textObject.all_speeches[count]['speechtitle'] == speech_title:
                speech_JSON = textObject.all_speeches[count]
                break
            count += 1
        return speech_JSON

    def turn_speech_string_to_list(self, speech_text):
        speech_in_list = list(speech_text.split(". "))
        return speech_in_list
