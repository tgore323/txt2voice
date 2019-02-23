'''
txt2voice by Tim Gore, KE6QBV@galvonix.com
version 0.5.0

txt2voice is a small python program to create channel announcement
files for use with Motorola two-way radios. Program creates MP3 files
which will need conversion to WAV files with proper formatting. (See
to-do items).

INSTRUCTIONS:

The text-to-speech engine used is Google's "gTTS". To install: 'pip3 install gtts'
If choosing to import a text file, make sure you use the full filename. For example. if
you want to import a text file called 'input' you would enter input.txt. The file must 
be located in the same directory as this python file.

IMPORTANT INFO REGARDING TEXT FILES: Make sure desired text file has no empty spaces 
at end of file, or you'll get an "AssertionError: No text to speak"

This program has only been tested with linux. I have no desire to make it work in 
Windows or MacOS. If you do, be my guest.

To-do items:
    - Handle error when user inputs a text file name that doesn't exist
    - Once files are made, do the nessassary conversion from inside program
    - GUI?
    - Have user supply file location instead of requiring the file to be in 
      same directory as program.
    - Handle error when there are blank lines at bottom of text file
'''

from gtts import gTTS # import Google's TTS

print("\nHow would you like to supply the source text? \n")
source = ''
# Loop until user quits.
while source != 'q':
    print("\n[1] From a text file.")
    print("[2] Manual entry.")
    print("[q] Quit txt2voice.")
    
    # User's choice of source
    source = input("\nEnter your selection: ")
    
    # If user chooses to import text file, ask for file name, then take each
    # line from file and generate MP3 files.
    if source == '1':
        list = []
        txt_filename = str(input("Please enter file name: "))
        list = open(txt_filename).read().splitlines()
        for x in range(len(list)):
            tts = gTTS(list[x], lang = "en")
            filename = list[x] + ".mp3"
            tts.save(filename)
    # If user chooses to manually input text, ask how many items to process.
    elif source == '2':
        list = []
        number = int(input("How many strings of text? "))
        for i in range(0, number):
            # Ask for manual input
            word = str(input("Please enter a string: "))
            list.append(word)
        # create voice files from text entered 
        for x in range(len(list)):
            tts = gTTS(list[x], lang = "en")
            filename = list[x] + ".mp3"
            tts.save(filename)
    # If user chooses to quit, then quit
    elif source == 'q':
        print("\nExiting program.\n")
    # What happens if user enters something other than 1, 2 or q
    else:
        print("\nInvalid input. Please try again.\n")
