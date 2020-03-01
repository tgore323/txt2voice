# txt2voice

txt2voice by Tim Gore, tgore323@gmail.com<br>
version 1.0.0 BETA<br>
3/1/2020<br>

txt2voice is a small python program to create channel announcement voice
files for use with Motorola two-way radios. This program creates WAV files that are 
compatable with Motorola MotoTrbo, XTS/XTL 5000 and APX series radios. 

INSTRUCTIONS:

The text-to-speech engine used is Google's "gTTS". To install: 'pip3 install gtts'

ffmpeg is required for converting the MP3 files that gtts outputs into compatable wav
files for the radios.

If choosing to import a text file, make sure you use the full path if the file is not in 
the same directory as this program. For an example, if the text file was in my home
directory I would enter /home/tim/textfilename.txt

IMPORTANT INFO REGARDING TEXT FILES: Make sure desired text file has no empty spaces 
at end of file, or you'll get an "AssertionError: No text to speak" (See to-do items).

This program has only been tested with linux. I have no desire to make it work in 
Windows or MacOS. If you do, be my guest.

TO-DO ITEMS / FEATURE WISHLIST:

- GUI?
- Strip blank lines in text input files
- Add Windows compatability (maybe)
- clean up code
- If ffmpeg isn't installed, prompt user to do so
- Add error reporting
- Interface with web interface
- Preferences and config files
