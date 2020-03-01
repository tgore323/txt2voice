import os
import glob
# files                                                                         
lst = glob.glob("*.mp3")
print(lst)
 
for file in lst:
# convert wav to mp3
	os.system(f"""ffmpeg -i {file} -acodec pcm_s16le -ar 8000 {file[:-4]}.wav""") 
# delete mp3 files after wav created
currentdir = os.getcwd() + '/*.mp3'
allmp3 = "rm *.mp3"
os.system(allmp3)



