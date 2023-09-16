#this is an automated script wholly for the education purpose.

#EXPLANATION: 
#        1. capture camera Image
#        2. transfer each pixel RGB data with color code to data frames
#        3. save the data in .csv file

import cv2
import pandas as pd

# Initialize the camera capture
cap = cv2.VideoCapture(0)  # Change the parameter to the camera index you want to use (0 for default camera)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Initialize an empty list to store pixel data
pixel_data = []

# Function to capture and process frames
def capture_and_process_frame():
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        return
    
    # Convert the frame to a DataFrame
    df = pd.DataFrame(frame.reshape(-1, 3), columns=['R', 'G', 'B'])
    
    # Append the pixel data to the list
    pixel_data.append(df)

# Capture a certain number of frames (you can modify the number of frames)
num_frames_to_capture = 10
for _ in range(num_frames_to_capture):
    capture_and_process_frame()

# Release the camera
cap.release()

# Concatenate the pixel data from all frames
pixel_data = pd.concat(pixel_data)

# Save the pixel data as a CSV file
pixel_data.to_csv('camera_pixels.csv', index=False)

print("Pixel data saved to camera_pixels.csv")

# Optionally, you can also display the first frame
cv2.imshow('First Frame', cv2.resize(pixel_data.iloc[0].to_numpy().reshape(frame.shape), (640, 480)))
cv2.waitKey(0)
cv2.destroyAllWindows()
