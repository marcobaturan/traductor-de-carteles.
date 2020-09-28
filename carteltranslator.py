"""Documentation.

    https://www.pyimagesearch.com/2020/09/14/getting-started-with-easyocr-for-optical-character-recognition/?__s=25xomddnz6q1gbwzghya
    https://github.com/JaidedAI/EasyOCR#supported-languages
    https://pypi.org/project/googletrans/
    https://www.jaided.ai/easyocr
"""
# Import.
import easyocr
from googletrans import Translator
import cv2
image = cv2.imread('images/chino.jpg')
trans = Translator()
# Need to run only once to load model into memory
reader = easyocr.Reader(['ch_tra','en']) 
# Add route to file to read and only show the resut in text.
results = reader.readtext(image)

  
def cleanup_text(text):
	# strip out non-ASCII text so we can draw the text on the image
	# using OpenCV
	return "".join([c if ord(c) < 128 else "" for c in text]).strip()
	
# loop over the results
for (bbox, text, prob) in results:
	# display the OCR'd text and associated probability
	print("[INFO] {:.4f}: {} = {}".format(prob, text,trans.translate(text, dest='es').text))
	# unpack the bounding box
	(tl, tr, br, bl) = bbox
	tl = (int(tl[0]), int(tl[1]))
	tr = (int(tr[0]), int(tr[1]))
	br = (int(br[0]), int(br[1]))
	bl = (int(bl[0]), int(bl[1]))
	# cleanup the text and draw the box surrounding the text along
	# with the OCR'd text itself
	#text = cleanup_text(text)
	cv2.rectangle(image, tl, br, (0, 255, 0), 2)
	cv2.putText(image, trans.translate(text, dest='es').text, (tl[0], tl[1] - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)


