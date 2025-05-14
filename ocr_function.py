import cv2           # handles all image loading and processing
import pytesseract   # python wrapper for Google's Tesseract-OCR Engine
import pyttsx3       # For converting text to speech (can be activated for audio output).
import time          # For potential timing/delay needs
import numpy as np   # For matrix-based image filtering, to enhance the image before running OCR.


# Specify the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_image_to_text(image_path, lang=None): # lang: Optional. Set 'ar' for Arabic text detection.
  # Path to the input image (PNG, JPG).
  image = cv2.imread(image_path)# Loads the image using OpenCV, Returns it as a NumPy array.  

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Simplifies the image by removing color, Improves OCR performance since text detection works better on single-channel images.
  # Optional: Enhance for OCR (adjust as needed)
  #  frame_enh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 85, 11) # Converts the image to a binary format, making it easier for OCR to detect text.

  laplacian_filter = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
  # Enhances the image by sharpening it, making text more distinct, Makes text stand out from the background for better recognition.
  # The filter is a 3x3 kernel that emphasizes edges in the image.
  frame_enh = cv2.filter2D(gray, -1, laplacian_filter) 

  # Perform OCR # Default is English.
  if lang == 'ar': 
    config = r'--psm 3 --oem 3 -l ara' # With Arabic: Specifies OCR language (-l ara), engine mode (--oem 3), and page segmentation mode (--psm 3).
    txt = pytesseract.image_to_string(frame_enh, config=config)
  else:
    txt = pytesseract.image_to_string(frame_enh)

  # Text-to-Speech
  # If OCR detects any text, return it, otherwise, return a fallback message.
  if txt:
    return txt
  else:
    return "Nothing To Read"

# Calls the ocr_image_to_text function with a sample image path.
# This is a test function to demonstrate the OCR functionality.
def test_ocr():
  print(ocr_image_to_text("static/logo.png"))


  """Key Features:
  - Supports Arabic OCR when specified.

  - Enhances images with filters for better accuracy.

  - Easily extendable to read the text aloud with pyttsx3 (can be activated).

  - Could be integrated into real-time camera input or smart glasses."""