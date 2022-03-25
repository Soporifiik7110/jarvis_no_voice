from gtts import gTTS


import os
tts = gTTS(text='démarage de la télévision', lang='fr')
tts.save("hello.mp3")
os.system("hello.mp3")