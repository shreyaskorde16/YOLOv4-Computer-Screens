import cv2
import os

# Function to extract frames from a video
def extract_images(video_path, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Check if the video file is opened successfully
    if not video.isOpened():
        print("Error opening video file")
        return

    frame_count =1

    # Read frames until the video ends
    while True:
        # Read the next frame
        ret, frame = video.read()

        # If frame is not read correctly or end of video is reached, exit the loop
        if not ret:
            break

        # Save the frame as an image
        frame_path = os.path.join(output_folder, f"frame{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)

        frame_count += 1

    # Release the video file
    video.release()
    print(f"Frames extracted: {frame_count}")

# Specify the video file path and output folder
video_path = "C:\Master's In Mechatronics\Student_Project_Image Recognition\Results_original\eight.avi"
output_folder = 'data_new8'

# Call the function to extract images from the video
extract_images(video_path, output_folder)