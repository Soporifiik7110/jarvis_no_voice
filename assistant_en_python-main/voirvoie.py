import pyttsx3
tts = pyttsx3.init("sapi5")
                                                #you can change the rate here
for voix in tts.getProperty("voices"):
    print(voix)
