#
# Program that takes text and turns it into speech. Speech is 
# saved as an MP3 file for later processing. 
# 
# We'll be using Google's TTS. (pip3 install gtts)
#
from gtts import gTTS

word = input("Enter text to be turned into speech: ")
tts = gTTS(text = word, lang = 'en')
filename = word + ".mp3"
tts.save(filename)






# Experimental workspace:

word_list = []
quantity = int(input("How many strings of text? "))
quantity = quantity - 1



# first_string = str(input("Enter string #1: "))
# second_string = str(input("Enter string #2: "))
# third_string = str(input("Enter string #3: "))


for i in range(0, quantity):
    word = str(input("Please enter a string: "))
    word_list.append(word)

