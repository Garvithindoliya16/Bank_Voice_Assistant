
from gtts import gTTS
import os


def speak(text):
	tts = gTTS(text, lang='hi')
	tts.save("output.mp3")
	os.system("mpg321 output.mp3")



if __name__ == "__main__":
    speak("आप क्या करना चाहते हैं")
    
	

