# from gtts import gTTS
# from PyPDF2 import PdfReader
# def pdf_to_text(pdf_file):
#     text = ""
#     with open(pdf_file, 'rb') as f:
#         reader = PdfReader(f)
#         for page_num in range(len(reader.pages)):
#             page = reader.pages[page_num]
#             text += page.extract_text()
#     return text
# def text_to_audio(text, output_file):
#     tts = gTTS(text)
#     tts.save(output_file)
# # Example usage:
# pdf_file = "speech.pdf"
# output_audio_file = "clcoding_audio1.mp3"
# text = pdf_to_text(pdf_file) 
# text_to_audio(text, output_audio_file)


import PyPDF2
import pyttsx3

with open('C:\\Users\\Admin\\OneDrive\\Desktop\\TestData\\Application_Form_ Identity_certificate.pdf', 'rb') as path:
    pdfreader = PyPDF2.PdfReader(path)
    speak = pyttsx3.init()
    for page_num in range(len(pdfreader.pages)):
        page = pdfreader.pages[page_num]
        text = page.extract_text()
        if text:
            print(f"\nReading page {page_num + 1}:\n")
            print(text)
            speak.say(text)
            speak.runAndWait()
        speak.stop()