Simulated Smart Glasses for Visually Impaired
Overview
This project, developed as a final year project for a Bachelor of Science in Artificial Intelligence at the Arab Open University - Egypt Branch, presents a software-based prototype simulating smart glasses to assist visually impaired individuals in navigating their environment independently. By leveraging existing devices like smartphones and webcams, the system provides real-time auditory feedback without requiring specialized hardware, enhancing accessibility and affordability. The project was completed by Ahmed Yasser Kamal Shaaban under the supervision of Dr. Ramdan Fawzy Mohamed Babers, achieving a comprehensive solution that integrates advanced computer vision and natural language processing technologies.

Features
Real-Time Object Detection: Utilizes YOLOv8 to detect and classify ~80 object classes, providing positional feedback (e.g., left, right, front) and distance estimation using real-world object dimensions.
Text Recognition (OCR): Employs Tesseract OCR to extract and read text aloud from images or documents using text-to-speech (pyttsx3), supporting printed text in English and Arabic.
Currency Recognition: Identifies Egyptian banknotes, aiding users in financial transactions, with a custom-trained YOLO model for accuracy.
Scene Description: Uses the BLIP model to generate natural language descriptions of environments, enhancing contextual awareness (e.g., "A chair is in front of you, a table to your right").
Voice Control: Supports hands-free operation via voice commands to switch modes (e.g., object detection, text reading, currency recognition) using the SpeechRecognition API.
Distance Estimation: Estimates object distances based on known dimensions, assisting with navigation and obstacle avoidance.
System Architecture
Frontend: Built with HTML, CSS, and JavaScript (Bootstrap for responsiveness), offering a user-friendly web interface with webcam integration and voice command support. The interface is designed for accessibility, with high-contrast colors and clear auditory feedback.
Backend: Developed using Flask (Python), integrating YOLOv8, Tesseract OCR, and BLIP models for processing and feedback generation. The backend handles real-time image processing and voice command interpretation, ensuring minimal latency.
Data Flow: Users upload images or stream webcam feeds, processed by the backend, with results delivered as auditory feedback via text-to-speech. The system follows a modular design, with clear separation of frontend and backend tasks, as detailed in the project’s use case and class diagrams.
Technologies Used
Programming Languages: Python, JavaScript
Frameworks/Libraries:
Flask: Web framework for backend
YOLOv8: Object detection and classification
Tesseract OCR: Text recognition
BLIP: Scene description
pyttsx3: Text-to-speech
SpeechRecognition API: Voice control
OpenCV: Image processing
num2words: Converts numeric counts to words for natural language output
Tools: Draw.io (diagrams), Bootstrap (frontend responsiveness), Jinja2 (Flask templating for dynamic content)
Development Methodology
The project followed the Waterfall Model SDLC, ensuring a structured approach:

Requirement Gathering: Identified functional (e.g., object detection, OCR) and non-functional (e.g., performance, accessibility) requirements.
System Design: Created use case, class, activity, and sequence diagrams to define the system architecture.
Implementation: Integrated YOLOv8, Tesseract, BLIP, and voice control, with Flask handling backend logic.
Testing: Conducted white box, black box, unit, system, and user acceptance testing.
Maintenance: Planned for bug fixes and feature enhancements based on user feedback.
Testing
The system underwent rigorous testing to ensure reliability and usability:

White Box Testing: Validated internal logic of YOLOv8, Tesseract, and currency models, ensuring accurate outputs.
Black Box Testing: Tested user interactions, voice commands, and overall system performance from an end-user perspective.
Unit Testing: Verified individual components (e.g., object detection, OCR, voice recognition) with test cases.
System Testing: Ensured seamless integration of frontend, backend, and models across various scenarios.
User Acceptance Testing: Conducted with visually impaired users to refine voice control, interface, and feedback clarity.
Challenges and Limitations
Lighting Conditions: Object detection and OCR accuracy decrease in low-light or cluttered environments. Mitigated by optimizing image preprocessing but requires further model training.
Currency Recognition: Struggles with worn or damaged notes, requiring a more robust model.
Voice Recognition: Less accurate in noisy environments, needing enhanced noise filtering.
Performance: Real-time processing can lag with high-resolution images. Optimized by adjusting resolution, but further improvements are needed.
Small Objects: Distance estimation is less accurate for small or distant objects due to camera limitations.
Future Work
Multilingual Support: Extend OCR and text-to-speech to support additional languages (e.g., Spanish, German) for global accessibility.
Improved Object Detection: Train YOLOv8 on diverse datasets to enhance accuracy in complex scenes, including small or occluded objects.
Hardware Integration: Pair with AR glasses for a seamless, immersive experience, reducing reliance on external devices.
Advanced Scene Understanding: Incorporate spatial relationships and contextual insights (e.g., "a person is sitting on a bench") for richer descriptions.
Real-Time Navigation: Integrate GPS or indoor mapping for turn-by-turn guidance and obstacle avoidance.
User Personalization: Allow users to customize detection sensitivity, speech speed, or prioritized objects.
Ethical Considerations
Privacy: No personal data is stored; images are processed locally or on the server without retention, adhering to data privacy regulations.
Accessibility: Designed for ease of use by visually impaired individuals, with voice control, high-contrast UI, and auditory feedback.
Inclusivity: Promotes independence and social inclusion by leveraging affordable, widely available devices.
Ethical Development: Involved visually impaired users in testing to ensure the system meets their needs, with a commitment to continuous improvement.