"""This script uses a pretrained transformer model from Hugging Face (BLIP) to automatically generate a textual description (caption) of an input image."""

from transformers import BlipProcessor, BlipForConditionalGeneration # Prepares the image for the model (resizing, normalization). , The core model that generates the caption.
from PIL import Image # For image processing and loading  is required by the processor (but isn't used explicitly — implicit conversion works).
import cv2

#  Loads the large BLIP model pretrained on image-captioning datasets, VQA , Downloads weights and processor from Hugging Face’s model hub.
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

# Generating a descriptive sentence that explains the content of the image.
def generate_caption_from_image(image_path): 

  # Path to the input image (PNG, JPG).
  image = cv2.imread(image_path)
  # Converts the image into tensor format for the model.
  inputs = processor(image, return_tensors="pt", max_new_tokens=100) # pt --> PyTorch format.
  out = model.generate(**inputs)
  caption = processor.decode(out[0], skip_special_tokens=True)
  return caption



def test_describe():
  print(generate_caption_from_image('static/logo.png'))