import cv2
import os
from dependency import get_bandwidth, show_popup_message

recording = False
frame_count = 0
output_directory = 'frames'
out = None

def start_recording():
    global recording, out, frame_count
    if not recording:
        recording = True
        frame_count = 0
        os.makedirs(output_directory, exist_ok=True)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')    # Defining the codec and create a VideoWriter object
        output_filename = os.path.join(output_directory, 'output_video.avi')
        frame_width = int(vid.get(3))
        frame_height = int(vid.get(4))
        out = cv2.VideoWriter(output_filename, fourcc, 24.0, (frame_width, frame_height))

def stop_recording():
    global recording, out

    if recording:
        recording = False
        if out is not None:
            out.release()
            out = None

vid = cv2.VideoCapture(0)  # # Initializing the video capture and using the default camera

# Main video loop
while True:
    ret, frame = vid.read()
    if recording:
        frame_filename = os.path.join(output_directory, f'frame_{frame_count:04d}.png') # Saving the frame as an image
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        start_recording()
        bandwidth = get_bandwidth()
        if bandwidth > 15:
            message = 'You are recording using Wi-Fi with speed >15mbps'
        else:
            message = 'You are using mobile hotspot <15mbps'
        print(message)
        show_popup_message(message)
    elif key == ord('p'):
        stop_recording()

vid.release()   # Releasing video capture and writer objects
if out is not None:
    out.release()

cv2.destroyAllWindows() # Close all OpenCV windows

output_video_filename = 'output_video.avi'  # Converting saved frames to video
first_frame_filename = os.path.join(output_directory, 'frame_0000.png')
first_frame = cv2.imread(first_frame_filename)
frame_height, frame_width, _ = first_frame.shape

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
output_video = cv2.VideoWriter(output_video_filename, fourcc, 24.0, (frame_width, frame_height))

for f in range(frame_count):
    frame_filename = os.path.join(output_directory, f'frame_{f:04d}.png') 
    frame = cv2.imread(frame_filename)
    output_video.write(frame)

output_video.release()
print(f"Video saved as {output_video_filename}")