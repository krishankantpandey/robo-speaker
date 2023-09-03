'''import pyttsx3  
engine = pyttsx3.init()  

print("Welcome to Robo Speaker 2.3.4. Created by KK")


text = input("Enter the text you want to say: ")


engine.say(text)  '''

import pyttsx3  
# initialize Text-to-speech engine  
engine = pyttsx3.init()  
# convert this text to speech
print("Welcome to Robo Speaker 2.3.4. Created by KK")
text = input("Enter the text you want to say: ")



engine.say(text)  
# play the speech  
engine.runAndWait()  

