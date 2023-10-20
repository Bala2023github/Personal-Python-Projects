import pyttsx3, PyPDF2

pdfreader = PyPDF2.PdfReader(open('book.pdf','rb'))

pages = len(pdfreader.pages)

print(pages)

speaker = pyttsx3.init()

for page_num in range(0,pages):

    page = pdfreader.pages[page_num]

    text = page.extract_text()
    # speaker.say(text)
    speaker.save_to_file(text,'audio.mp3')
    speaker.runAndWait()

#     clean_text = text.strip().replace('\n',' ')
#     print(clean_text)

# speaker.save_to_file(clean_text,'audio.mp3')
# speaker.runAndWait()

speaker.stop()