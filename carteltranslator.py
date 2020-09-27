"""Documentation.

    https://www.pyimagesearch.com/2020/09/14/getting-started-with-easyocr-for-optical-character-recognition/?__s=25xomddnz6q1gbwzghya
    https://github.com/JaidedAI/EasyOCR#supported-languages
    https://pypi.org/project/googletrans/
    https://www.jaided.ai/easyocr
"""
# Import.
import easyocr
from googletrans import Translator
import PySimpleGUI as sg

sg.theme('Light Blue 2')

layout = [[sg.Text('Enter 2 files to comare')],
          [sg.Text('File 1', size=(8, 1)), sg.Input(), sg.FileBrowse()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('File Compare', layout)

event, values = window.read()
window.close()

translator = Translator()
# Need to run only once to load model into memory
reader = easyocr.Reader(['fr','en'], gpu = False) 
# Add route to file to read and only show the resut in text.
result = reader.readtext(values[0],detail=0)
# Add translates the result.
translator.detect(result)