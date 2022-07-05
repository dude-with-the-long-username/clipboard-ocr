
# TODO: fix issue: will fail if latest clipboard entry is not an image
from fileinput import filename
import subprocess
from PIL import Image
import pytesseract
import numpy as np

command = 'rm -f screenshot_for_ocr_temp_file.png' # deleting file if it exists (tries even if it doesn't exist)
subprocess.call(command, shell=True)

command = 'xclip -selection clipboard -t image/png -o > screenshot_for_ocr_temp_file.png'  # outputs image in clipboard to screenshot_for_ocr_temp_file.png (if image exists in clipboard)
# TODO: program will break if file "screenshot_for_ocr_temp_file.png" already exists
subprocess.call(command, shell=True)

filename = 'screenshot_for_ocr_temp_file.png'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
# print(text)

