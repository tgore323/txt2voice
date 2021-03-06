from gtts import gTTS # import Google's TTS
import os # for file system access
from time import sleep # for delaying program output
import glob

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
    source = source.lower()

    # If user chooses to import text file, ask for file name, then take each
    # line from file and generate MP3 files.
    if source == '1':
        list = []
        cwd = os.getcwd()
        print("\nYour current working directory is: \n ")
        print(cwd)
        txt_filename = str(input("\nPlease enter the location of your text file: "))
        os.path.isfile(txt_filename)
        if os.path.isfile(txt_filename) == True:
            list = open(txt_filename).read().splitlines()
            for x in range(len(list)):
                tts = gTTS(list[x], lang = "en")
                filename = list[x] + ".mp3"
                filename = filename.replace(" ", "_")
                filename = filename.lower()
                tts.save(filename)
                print("\nCreating file: " + filename)
                lst = glob.glob("*.mp3")
                print(lst)
                for file in lst:
                # convert wav to mp3
	                os.system(f"""ffmpeg -i {file} -acodec pcm_s16le -ar 8000 {file[:-4]}.wav""") 
                # delete mp3 files after wav created
                currentdir = os.getcwd() + '/*.mp3'
                allmp3 = "rm *.mp3"
                os.system(allmp3)
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
            word = word.lower()
            list.append(word)
        # create voice files from text entered
        for x in range(len(list)):
            tts = gTTS(list[x], lang = "en")
            filename = list[x] + ".mp3"
            filename = filename.replace(" ", "_")
            tts.save(filename)
            print("\nCreating file: " + filename)
            lst = glob.glob("*.mp3")
            print(lst)
            for file in lst:
                # convert wav to mp3
	            os.system(f"""ffmpeg -i {file} -acodec pcm_s16le -ar 8000 {file[:-4]}.wav""")
                # Display help.txt which is located in program root directory
            currentdir = os.getcwd() + '/*.mp3'
            allmp3 = "rm *.mp3"
            os.system(allmp3)
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
