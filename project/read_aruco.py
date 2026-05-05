import cv2
import numpy as np

# Initialize webcam (0 = default camera)
cam = cv2.VideoCapture(0)

# Capture one frame
ret, frame = cam.read()

if ret:
    cv2.imshow("Captured", frame)         
    cv2.imwrite("captured_image.png", frame)  
    cv2.waitKey(0)                      
    cv2.destroyWindow("Captured")       
else:
    print("Failed to capture image.")

cam.release()

# Load the image
image = cv2.imread('captured_image.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
parameters = cv2.aruco.DetectorParameters()

# Create the ArUco detector
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
# Detect the markers
corners, ids, rejected = detector.detectMarkers(gray)
# Print the detected markers
print("Detected markers:", ids)
if ids is not None:
    cv2.aruco.drawDetectedMarkers(image, corners, ids)
    for e in zip(corners,ids):
        x1, y1 = e[0][0][0]
        x2, y2 = e[0][0][2]
        x = (x1 + x2) / 2
        y = (y1 + y2) / 2
        image = cv2.circle(image, (int(x),int(y)), radius=2, color=(0, 0, 255), thickness=-1)
    cv2.imshow('Detected Markers', image)
    cv2.imwrite("aruco_image.png", image) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()