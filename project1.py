#reading text file
#creating audio txt file
#pyttsx3 - text to speech conversion library in python
import pyttsx3
book = open(r"C:\Users\archa\OneDrive\Desktop\file.txt")
book_text = book.readlines()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()
