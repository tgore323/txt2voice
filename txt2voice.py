'''
txt2voice by Tim Gore, KE6QBV@galvonix.com
version 0.5.3    2/26/2018

txt2voice is a small python program to create channel announcement
files for use with Motorola two-way radios. This program creates MP3 files
which will need conversion to WAV files with proper formatting. (See
to-do items). 

INSTRUCTIONS:

The text-to-speech engine used is Google's "gTTS". To install: 'pip3 install gtts'

If choosing to import a text file, make sure you use the full path if the file is not in 
the same directory as this program. For an example, if the text file was in my home
directory I would enter /home/tim/textfilename.txt

IMPORTANT INFO REGARDING TEXT FILES: Make sure desired text file has no empty spaces 
at end of file, or you'll get an "AssertionError: No text to speak" (See to-do items).

This program has only been tested with linux. I have no desire to make it work in 
Windows or MacOS. If you do, be my guest.

To-do items:
    - Once files are made, do the nessassary conversion from inside program
    - GUI?
    - Handle error when there are blank lines at bottom of text file (or just remove them).
'''

from gtts import gTTS # import Google's TTS
import os.path # for file system access
from time import sleep # for delaying program output

print("\nHow would you like to supply the source text? \n")
source = ''
# Menu to choose text source or quit
while source != 'q':
    print("\n[1] From a text file.")
    print("[2] Manual entry.")
    print("[h] View help.")
    print("[q] Quit txt2voice.")
    
    # User's choice of source
    source = input("\nEnter your selection: ")
    
    # If user chooses to import text file, ask for file name, then take each
    # line from file and generate MP3 files.
    if source == '1':
        list = []
        txt_filename = str(input("\nPlease enter the file's location: "))
        os.path.isfile(txt_filename)
        if os.path.isfile(txt_filename) == True:
            list = open(txt_filename).read().splitlines()

            for x in range(len(list)):
                tts = gTTS(list[x], lang = "en")
                filename = list[x] + ".mp3"
                tts.save(filename)
        else:
            print("\nThe location you entered is not valid. Please try again. \n")
            sleep(2)

    # If user chooses to manually input text, ask how many items to process.
    elif source == '2':
        list = []
        number = int(input("How many voice files would you like to create? "))
        for i in range(0, number):
            # Ask for manual input
            word = str(input("Please enter a string of text: "))
            list.append(word)
        # create voice files from text entered 
        for x in range(len(list)):
            tts = gTTS(list[x], lang = "en")
            filename = list[x] + ".mp3"
            tts.save(filename)
    # Display help.txt which is located in program root directory
    elif source == 'h':
        if os.path.isfile("help.txt") == True:
            f = open('help.txt', 'r')
            help_contents = f.read()
            print (help_contents)
            f.close()
            input("\nPress ENTER to return to the main menu.\n")
        else:
            input("\nERROR: File help.txt not found. Press ENTER to return to the main menu.\n")
    # If user chooses to quit, then quit
    elif source == 'q':
        print("\nExiting program.\n")
    # What happens if user enters something other than 1, 2 or q
    else:
        print("\nInvalid input. Please try again.\n")

