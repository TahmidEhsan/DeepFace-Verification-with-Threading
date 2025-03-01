import threading  # Import threading for parallel execution
import cv2  # Import OpenCV for video capture and image processing
from deepface import DeepFace  # Import DeepFace for face verification

# Initialize video capture from the default camera (0)
cap = cv2.VideoCapture(0)  
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set video width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set video height

counter = 0  # Frame counter to control face verification frequency
faceMatch = False  # Boolean flag to store face match result
lock = threading.Lock()  # Thread lock to ensure safe variable access

# Load reference image for face comparison
reference_img = cv2.imread("reference.JPG")  
if reference_img is None:
    raise ValueError("Reference image not found or invalid file format.")

# Function to verify face match in a separate thread
def checkFace(frame):
    global faceMatch
    try:
        # Perform face verification
        result = DeepFace.verify(frame, reference_img.copy())['verified']
        with lock:  # Lock to prevent race conditions
            faceMatch = result
    except Exception as e:
        print(f"Error in face verification: {e}")
        with lock:
            faceMatch = False  # Default to no match if an error occurs

# Main video capture loop
while True:
    ret, frame = cap.read()  # Capture frame from webcam
    if not ret:
        print("Failed to capture frame")
        break  # Exit loop if frame capture fails
    
    # Perform face verification every 30 frames
    if counter % 30 == 0:
        threading.Thread(target=checkFace, args=(frame.copy(),), daemon=True).start()
    counter += 1  # Increment frame counter
    
    # Display face match result on video feed
    with lock:
        match_text = "MATCH!" if faceMatch else "NO MATCH!"
        color = (0, 255, 0) if faceMatch else (0, 0, 255)  # Green for match, red for no match
    
    cv2.putText(frame, match_text, (20, 450), cv2.FONT_HERSHEY_COMPLEX, 2, color, 3)
    cv2.imshow("video", frame)  # Show video feed with match status
    
    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources after exiting loop
cap.release()
cv2.destroyAllWindows()
