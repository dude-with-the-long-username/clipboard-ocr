
# TODO: fix issue: will fail if latest clipboard entry is not an image
# TODO: fix: don't create temporary files
from fileinput import filename
import subprocess
from PIL import Image
import pytesseract
import numpy as np

command = 'rm -f screenshot_for_ocr_temp_file.png' # deleting file if it exists (tries even if it doesn't exist)
subprocess.call(command, shell=True)

command = 'xclip -selection clipboard -t image/png -o > screenshot_for_ocr_temp_file.png'  # outputs image in clipboard to screenshot_for_ocr_temp_file.png (if image exists in clipboard)
subprocess.call(command, shell=True)

filename = 'screenshot_for_ocr_temp_file.png'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
# print(text)

with open ('text_obtained_from_ocr.txt', 'w') as output_file:
    output_file.write(text)

command = 'cat text_obtained_from_ocr.txt | xclip -selection clipboard'
subprocess.call(command, shell=True)



# deleting both temporary files
command = 'rm -f screenshot_for_ocr_temp_file.png text_obtained_from_ocr.txt' # deleting file if it exists (tries even if it doesn't exist)
subprocess.call(command, shell=True)
