import pyttsx3, PyPDF2

# open pdf file and assign it to a variable
reader = PyPDF2.PdfReader('prayer.pdf')

# initiate speaker
speaker = pyttsx3.init()

for page_num in range(len(reader.pages)):
    text = reader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text,'prayer.mp3')

speaker.runAndWait()
speaker.stop()


