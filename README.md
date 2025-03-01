# DeepFace Real-Time Face Verification with Threading

## Overview

This project implements a real-time face verification system using **DeepFace** and **OpenCV**, with optimized threading for improved performance. The system captures live video feed, processes frames asynchronously, and checks for a match against a reference image.

## Features

- **Multi-threaded Face Recognition**: Uses `threading` to prevent frame processing lag.
- **Real-Time Verification**: Captures video from a webcam and verifies faces every 30 frames.
- **Optimized Performance**: Implements thread locks to prevent race conditions.
- **Dynamic Feedback**: Displays `MATCH!` or `NO MATCH!` on the video stream.
- **Robust Error Handling**: Handles missing reference images and DeepFace errors gracefully.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- DeepFace (`pip install deepface`)
- Threading (built-in Python module)

## Setup & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/TahmidEhsan/deepface-threading.git
   cd deepface-threading
   ```
2. Install dependencies:
   ```bash
   pip install deepface opencv-python
   ```
3. Add a **reference image** named `reference.jpg` to the project directory.
4. Run the script:
   ```bash
   python face_verification.py
   ```

## Future Improvements

- Implement **multi-user recognition** by storing multiple reference images.
- Add **emotion detection** and **age/gender analysis**.
- Integrate with **IoT devices** for security automation.

## License

This project is licensed under the MIT License.

