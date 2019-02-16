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
# if len(word) is >= 1:
#     print("long")
# else:
#     print("short")
