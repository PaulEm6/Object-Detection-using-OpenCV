import cv2
import numpy as np
import os, sys

if len(sys.argv) != 2:
    print("Usage: python script.py /path/to/file")
else:
    file_path = sys.argv[1]
    if os.path.exists(file_path) == False:
        print("Image file does not exist.")

#WORKS ONLY IF IMAGE AND REFERENCE IMAGE IN SAME DIRECTORY
directory = os.path.dirname(file_path)
reference = os.path.join(directory,"Reference.jpg")

if os.path.exists(reference) == False:
    print("Reference Image not found")

# Load the room image (without objects) and the image with objects
room_image = cv2.imread(reference)
image_path = file_path
object_image = cv2.imread(image_path)

# Define the center-biased Gaussian filter parameters
kernel_size = (15, 15)  # Adjust the kernel size as needed
sigma = 40  # Adjust the sigma value for the desired effect

# Define the kernel for the opening operation
kernel_size_2 = (15, 15)  # Adjust the kernel size as needed
kernel = np.ones(kernel_size_2, np.uint8)

# Convert both images to grayscale
room_gray = cv2.cvtColor(room_image, cv2.COLOR_BGR2GRAY)
object_gray = cv2.cvtColor(object_image, cv2.COLOR_BGR2GRAY)

# Compute the absolute difference between the two grayscale images
difference = cv2.absdiff(room_gray, object_gray)

################ APPLYING FILTERS #######################

# Apply the Gaussian filter to the image to remove noise in background
difference = cv2.GaussianBlur(difference, kernel_size, sigma)

# Apply the opening filter to remove noise in background and small objects in background
difference = cv2.morphologyEx(difference, cv2.MORPH_OPEN, kernel)

##########################################################

# Apply a threshold to the difference image to remove useless information
_, thresholded = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding boxes around the detected objects
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    min_area_limit = 10000
    max_area_limit = 5000000
    if w * h > min_area_limit and w * h < max_area_limit :  # Filter out small artifacts and artificats that are too big
        cv2.rectangle(object_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Save or display the room image with bounding boxes
cv2.imwrite(str(file_path) + '_objects_detected.jpg', object_image)

