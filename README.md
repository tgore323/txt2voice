# txt2voice

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
at end of file, or you'll get an "AssertionError: No text to speak" (see to-do)

This program has only been tested with linux. I have no desire to make it work in 
Windows or MacOS. If you do, be my guest.

TO-DO LIST:
- Handle error when user inputs a text file name that doesn't exist
- Once files are made, do the nessassary conversion from inside program (ffmpeg?)
- GUI?
- Have user supply file location instead of requiring the file to be in same directory as program.
- Handle error when there are blank lines at bottom of text file
- Show progress of conversion. Verbose perhaps?
