# DeepFace-Verification-with-Threading

Overview

This project implements a real-time face verification system using DeepFace and OpenCV, with optimized threading for improved performance. The system captures live video feed, processes frames asynchronously, and checks for a match against a reference image.

Features
-Multi-threaded Face Recognition: Uses threading to prevent frame processing lag.
-Real-Time Verification: Captures video from a webcam and verifies faces every 30 frames.
-Optimized Performance: Implements thread locks to prevent race conditions.
-Dynamic Feedback: Displays MATCH! or NO MATCH! on the video stream.
-Robust Error Handling: Handles missing reference images and DeepFace errors gracefully.

Requirements
-Python 3.x
-OpenCV (cv2)
-DeepFace (pip install deepface)
-Threading (built-in Python module)

Setup & Usage
-Clone the repository: git clone https://github.com/TahmidEhsan/deepface-threading.git
cd deepface-threading
-Install dependencies: pip install deepface opencv-python
-Add a reference image named reference.jpg to the project directory.
-Run the script: python face_verification.py
-Press q to exit the program.
