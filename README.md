# txt2voice

txt2voice by Tim Gore, KE6QBV@galvonix.com<br>
version 0.5.4<br>
3/1/2019<br>

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
- Convert MP3 to wav (currently in alpha via converter.py)
- Create wav files that need tno further external conversion
- GUI?
- Handle error when there are blank lines at bottom of text file (or just remove them).
