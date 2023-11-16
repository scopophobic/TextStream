import cv2
import numpy as np

# Function to convert text to binary chunks
def text_to_binary_chunks(text, chunk_size):
    binary_chunks = [format(ord(char), '08b') for char in text]
    return [''.join(binary_chunks[i:i+chunk_size]) for i in range(0, len(binary_chunks), chunk_size)]

# Function to create frames from binary chunks
def create_frames_from_chunks(binary_chunks, width, height):
    frames = []
    for chunk in binary_chunks:
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        chunk_size = min(len(chunk), width * height // 4)  # Each bit represented by 4 pixels
        for i in range(chunk_size):
            x = (i * 2) % width
            y = (i * 2) // width * 2
            color = (255, 255, 255) if chunk[i] == '1' else (0, 0, 0)
            cv2.rectangle(frame, (x, y), (x + 1, y + 1), color, -1)
            cv2.rectangle(frame, (x + 1, y), (x + 2, y + 1), color, -1)
            cv2.rectangle(frame, (x, y + 1), (x + 1, y + 2), color, -1)
            cv2.rectangle(frame, (x + 1, y + 1), (x + 2, y + 2), color, -1)
        frames.append(frame)
    return frames

# Read text from file
text_file_path = 'input/input.txt'
with open(text_file_path, 'r') as file:
    text_content = file.read()

# Define video frame dimensions
width, height = 640, 480
frame_count = 100  # Number of frames for encoding
fps = 1  # Frames per second
chunk_size = 10000  # Define the chunk size for binary representation

# Convert text content to binary chunks
binary_chunks = text_to_binary_chunks(text_content, chunk_size)

# Create a VideoWriter object with MP4 codec
out = cv2.VideoWriter('encoded_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

# Create frames from binary chunks
frames = create_frames_from_chunks(binary_chunks, width, height)

# Write frames to the video
for frame in frames:
    out.write(frame)

# Release the VideoWriter object
out.release()
