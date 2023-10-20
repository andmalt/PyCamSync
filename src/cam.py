from configparser import RawConfigParser
import os
import time
import cv2
from datetime import datetime
from src.zip import zip_video

def record_video(config:RawConfigParser,fps:float,args_time):
    folder = str(config["FOLDERS"]["DIR"])
    # modified_size = size.split(',')
    # frame_size = [int(size) for size in modified_size]
    # print(frame_size)
    print("Waiting....")
    # Turn on the webcam
    webcam = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not webcam.isOpened():
        print("Unable to access the webcam")
        return

    date = datetime.now()
    formatted_data = date.strftime("%Y-%m-%d_%H-%M-%S-%f")
    video_filename  =  f"video_{formatted_data}.avi"
    # print(video_filename)
    
    directory_path = os.path.join(folder, "Compressed")
    # create directory if it doesn't exist
    try:
        os.makedirs(directory_path)
    except:
        pass
    
    video_path = os.path.join(folder,video_filename)
    # Set the codec and create a VideoWriter object to save the video
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # Leave the frame size in the default configuration, because if it is changed it will not work.
    out = cv2.VideoWriter(video_path, fourcc, fps, [640,480])
    print('Video is recording')
    start_time = time.time()
    max_time = args_time
    while True:
        elapsed_time = time.time() - start_time
        # Read a frame from the webcam
        ret, frame = webcam.read()

        if ret:
            # Write the frame in the video
            out.write(frame)

            # View the frame
            cv2.imshow("Webcam", frame)
        # Stop recording if 'q' button is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if elapsed_time >= max_time:
            break

    # Release resources
    webcam.release()
    out.release()
    cv2.destroyAllWindows()
    print("The video is recorded")
    zip_video(config,video_path,video_filename)
