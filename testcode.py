from gtts import gTTS

word_list = []
quantity = int(input("How many strings of text? "))
for i in range(0, quantity):
    word = str(input("Please enter a string: "))
    word_list.append(word)
tts = gTTS(text = word, lang = 'en')
filename = word + ".mp3"
tts.save(filename)

# to do:
# pass each list item into gtts. currently only generates last
# item in list
#