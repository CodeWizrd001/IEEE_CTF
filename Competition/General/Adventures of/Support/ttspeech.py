import pyttsx3
from gtts import gTTS 

import os 
  
mytext = """
I'm Zeus and this is fate . And to meet you three is the current fate . 
said Zeus .
You've come a long way and want answers .
We'll guide to one 
But are responsible for none
said Fate .

The password to the zip file is 1 2 3 5 4 1

If you have listened to us 
You know what to do
Go my friends
Let fate be with you
"""
  
language = 'en'
  
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
myobj.save("clue.mp3") 
os.system("mpg321 clue.mp3") 
