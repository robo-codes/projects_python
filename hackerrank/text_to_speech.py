from gtts import gTTS
import os
text = str(input())
#print(googletrans.LANGUAGES)
'''translator = Translator()
translated = translator.translate(text, src = 'en', dest = 'gu')
#print(translated.text)
speech = gTTS(text = text, lang = language, slow = False)
speech.save("test.mp3")
os.system("start test.mp3")'''
language = 'en'
speech = gTTS(text = text, lang = language, slow = False)
speech.save("test.mp3")
os.system("start test.mp3")
