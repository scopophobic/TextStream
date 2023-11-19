import cv2
import numpy as np

def extract_binary_from_frame(frame):
    binary_chunk = ''
    for y in range(0, frame.shape[0], 4):
        for x in range(0, frame.shape[1], 4):
            block = frame[y:y + 4, x:x + 4, 0]  # Assuming black/white encoding
            bit = '1' if np.mean(block) > 127 else '0'
            binary_chunk += bit
    return binary_chunk

def read_frames_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    binary_chunks = []
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        binary_chunk = extract_binary_from_frame(frame)
        binary_chunks.append(binary_chunk)
    
    cap.release()
    return binary_chunks

def binary_to_text(binary_data):
    text = ''
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i + 8]
        text += chr(int(byte, 2))
    return text

# Specify the video file path
video_file_path = 'input_video/encoded_video.mp4'

# Read frames from the video and retrieve binary chunks
retrieved_chunks = read_frames_from_video(video_file_path)

# Convert binary chunks back to text
decoded_text = binary_to_text(''.join(retrieved_chunks))

# Print or use the decoded text
# print(decoded_text)   ## this is output

output_file_path = 'output/decoded_text.txt'
decoded_text = decoded_text.strip()
# Write the decoded text to a text file
with open(output_file_path, 'w') as file:
    file.write(decoded_text)

print("Decoded text has been written to", output_file_path)