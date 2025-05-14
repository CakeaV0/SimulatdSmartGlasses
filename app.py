# ---------------------------------------
# Import Libraries ----------------------
# ---------------------------------------
import os
import shutil
from datetime import datetime
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from ultralytics import YOLO
from waitress import serve

from finder_and_depth_estimation import find, test_find
from detection_function import *
from describe_function_2 import generate_caption_from_image, test_describe
from ocr_function import ocr_image_to_text, test_ocr
from summarize_function import summarize_text, test_summarize

# ---------------------------------------
# Initialize Flask App and Model --------
# ---------------------------------------
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
model = YOLO("yolov8m.pt")

# ---------------------------------------
# Test Program Functions ----------------
# ---------------------------------------
def test_program_functions():
    print("Testing the Description Mode ............")
    test_describe()
    print("Done ✔️")
    print("Testing the OCR Text Mode ............")
    test_ocr()
    print("Done ✔️")
    print("Testing the Summarize Text Mode ............")
    test_summarize()
    print("Done ✔️")
    print("Testing the Finder Mode ............")
    test_find()
    print("Done ✔️")
    print("Testing the Detection Mode ............")
    test_detection()
    print("Done ✔️")
    print("---------------------------------------------------")
    print("The Program Is Ready ✔️ ---------------------------")
    print("---------------------------------------------------")

test_program_functions()

# ---------------------------------------
# Helper Functions ----------------------
# ---------------------------------------
def save_file(file):
    today_date = datetime.now().strftime('%Y-%m-%d')
    today_folder_path = os.path.join(UPLOAD_FOLDER, today_date)
    os.makedirs(today_folder_path, exist_ok=True)

    # Remove folders with names other than today's date
    for folder in os.listdir(UPLOAD_FOLDER):
        folder_path = os.path.join(UPLOAD_FOLDER, folder)
        if os.path.isdir(folder_path) and folder != today_date:
            shutil.rmtree(folder_path)

    # Save the image with the current datetime
    filename = secure_filename(file.filename)
    filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S_') + filename
    file_path = os.path.join(today_folder_path, filename)
    file.save(file_path)
    return os.path.join(today_folder_path, filename)

def process_detected_text(detected_text):
    # Example: Clean up the text by removing extra spaces or unwanted characters
    cleaned_text = " ".join(detected_text.split())
    
    # Example: Validate the text (e.g., check if it contains specific keywords)
    if "important" in cleaned_text.lower():
        return f"{cleaned_text} (validated as important)"
    
    # Example: Perform additional analysis or transformations
    return cleaned_text

# ---------------------------------------
# Routes --------------------------------
# ---------------------------------------
@app.route('/', methods=['GET'])
def index():
    names = model.names
    return render_template('index.html', names=names)

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify([{'result': 'No image received', 'mode': 'object'}])

    f = request.files['image']
    selected_option = request.form.get('select_mode')
    object_to_be_found = request.form.get('object_to_be_found')

    file_path = save_file(f)

    # Process using selected mode
    if selected_option == "currency":
        result = image_detection(file_path, "currency")
    elif selected_option == "describe":
        result = generate_caption_from_image(file_path)
    elif selected_option == "text":
        # Detect text and process it
        detected_text = ocr_image_to_text(file_path)
        processed_text = process_detected_text(detected_text)  # Additional processing logic
        result = f"{processed_text}"
    elif selected_option == "summarize":
        result = summarize_text(file_path)
    elif selected_option == "find":
        result = find(file_path, object_to_be_found)
    elif selected_option == "object":
        result = image_detection(file_path, "object")

    return jsonify([{'result': result, 'mode': selected_option}])

# ---------------------------------------
# Run The App ---------------------------
# ---------------------------------------
if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5001
    app.run(host=host, port=port, debug=True)
