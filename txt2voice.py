'''
txt2voice by Tim Gore, KE6QBV

txt2voice is a small python program to create channel announcement
files for use Motorola two-way radios. 

INSTRUCTIONS:

The text-to-speech engine used is Google's "gTTS". To install: 'pip3 install gtts'
If choosing to import a text file, make sure you use the full filename. For example. if
you want to import a text file called 'input' you would enter input.txt. The file must 
be located in the same directory as this python file.

This program has only been tested with linux. I have no desire to make it work in 
Windows or MacOS. If you do, be my guest.

To-do items:
    - Once files are made, do the nessassary conversion from inside program
    - GUI?

'''

from gtts import gTTS

print("Please choose how you would like to input text: \n")
answer_1 = input("a) From a text file\nb) Manually\n:")
if answer_1.lower() == "a":
    list = []
    txt_filename = str(input("Please enter file name: "))
    list = open(txt_filename).read().splitlines()
    for x in range(len(list)):
        tts = gTTS(list[x], lang = "en")
        filename = list[x] + ".mp3"
        tts.save(filename)
else:
    list = []
    number = int(input("How many strings of text? "))
    for i in range(0, number):
        word = str(input("Please enter a string: "))
        list.append(word)
    for x in range(len(list)):
        tts = gTTS(list[x], lang = "en")
        filename = list[x] + ".mp3"
        tts.save(filename)


