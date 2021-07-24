import os 
from ocrproj.settings import BASE_DIR
from PIL import Image
import pytesseract
from django.core.files.storage import default_storage


pytesseract.pytesseract.tesseract_cmd = str(BASE_DIR) + r"\ocr-engine\tesseract.exe"


def convertimg(file_name,lang, f):
	if file_name.endswith('.jpg') or file_name.endswith('.png') or file_name.endswith('.jpeg'):
		response = {}
		file_name_2 = default_storage.save(file_name, f)
		file_url = default_storage.url(file_name_2)
		image_to_text = pytesseract.image_to_string(BASE_DIR + '//' + file_url, lang=lang)
		response['name'] = str(image_to_text).strip()
		print(response['name'])
		os.remove(file_url)
	else:
		response['name'] = "this filetype is not supported please attach jpg or png!"

	return response