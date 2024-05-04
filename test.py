from melo.api import TTS
from PyPDF2 import PdfReader
import time

# Speed is adjustable
speed = 1.0
device = 'cpu' # or cuda:0

text = "How about management? Do you enjoy managing people? Do you enjoy making engineering processes more efficient?"
model = TTS(language='EN', device=device)
speaker_ids = model.hps.data.spk2id


reader = PdfReader("example.pdf")

text = ''
number_of_pages = len(reader.pages)
for pageNum in range(10, 11):
  page = reader.pages[pageNum].extract_text().replace('-\n', '')
  page = page.replace('\n', '')
  print(page)
  # American accent
  text = text + page
  print('finish one page')
print("the end")
output_path = 'output-test.wav'

t1 = time.time()
model.tts_to_file(text, speaker_ids['EN-US'], output_path, speed=speed)
t2 = time.time()
print(t2-t1)