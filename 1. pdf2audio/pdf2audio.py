#import Pyttsx3
import PyPDF2
# pyttsx3 is a text-to-speech conversion library in Python
# PyPDF2 is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files.

from PyPDF2 import PdfReader

reader = PdfReader("book.pdf")
page = reader.pages[0]
text = page.extract_text()
print(text)

# open pdf file
#pdfreader1 = PyPDF2.PdfReader(open('book.pdf'),'rb')
#pdfreader1 = PyPDF2.PdfReader('book.pdf')
# initializing speaker
#engine = pyttsx3.init()

#for page_num in range(pdfreader1.numPages):
#    text = pdfreader1.getPage(page_num).extractText()
#    clean_text = text.strip().replace('\n','')
#    print(clean_text)

import pyttsx3
engine = pyttsx3.init()
#engine = pyttsx3.init('dummy')
""" engine.save_to_file('Hello World' , 'test.mp3')
engine.runAndWait()
 """
engine.save_to_file(text,'audio.mp3')
engine.runAndWait()

engine.stop()