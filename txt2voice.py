'''
txt2voice by Tim Gore, KE6QBV

txt2voice is a small python program to create voice files from inputed text. These
voice files can then be converted to channel announcements for use Motorola two-way
radios. 

The text-to-speech engine used is Google's "gTTS". To install: 'pip3 install gtts'

This program has only been tested with linux. I have no desire to make it work in 
Windows or MacOS

To-do items:
    - allow users to input a CSV or text file instead of entering each text string individually
    - Once files are made, do the nessassary conversion from inside program
'''

from gtts import gTTS

# create a list and find out how many files to make
list = []
number = int(input("How many strings of text? "))

# get text for desired voice file(s)
for i in range(0, number):
    word = str(input("Please enter a string: "))
    list.append(word)

# create voice files
for x in range(len(list)):
    tts = gTTS(list[x], lang = "en")
    filename = list[x] + ".mp3"
    tts.save(filename)
