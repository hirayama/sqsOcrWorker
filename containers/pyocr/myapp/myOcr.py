from PIL import Image
import sys

import pyocr
import pyocr.builders
import re
import urllib.request
import urllib.parse
import os

def my_ocr(url):
  filename = os.path.basename(urllib.parse.urlparse(url).path)
  image_path = os.path.dirname(os.path.abspath(__file__)) + '/image/tmp_' + filename
  urllib.request.urlretrieve(url, image_path)
  tools = pyocr.get_available_tools()
  if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
  tool = tools[0]
  langs = tool.get_available_languages()
  lang = langs[0]
  img = Image.open(image_path)
  img_width, img_height = img.size
  target = img.crop((0,img_height*0.9,500,img_height))
  txt = tool.image_to_string(
    target,
    lang="eng",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
  )
  return {
    'url': url,
    'filename': filename,
    'ocr_value': re.search(r"(?!0)[0-9]+$", txt).group(),
  }
    
