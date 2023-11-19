import cv2
import numpy as np

def text_to_binary_chunks(text, chunk_size):
    binary_chunks = [format(ord(char), '08b') for char in text]
    return [''.join(binary_chunks[i:i+chunk_size]) for i in range(0, len(binary_chunks), chunk_size)]

def create_frames_from_chunks(binary_chunks, width, height):
    frames = []
    for chunk in binary_chunks:
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        chunk_size = min(len(chunk), width * height // 16)  # Each bit represented by 16 pixels (4x4)
        for i in range(chunk_size):
            x = (i * 4) % width
            y = (i * 4) // width * 4
            color = (255, 255, 255) if chunk[i] == '1' else (0, 0, 0)
            for m in range(4):
                for n in range(4):
                    cv2.rectangle(frame, (x + m, y + n), (x + m + 1, y + n + 1), color, -1)
        frames.append(frame)
    return frames

text_file_path = 'input/input.txt'
with open(text_file_path, 'r') as file:
    text_content = file.read()

width, height = 640, 480
frame_count = 100
fps = 1
chunk_size = 10000

binary_chunks = text_to_binary_chunks(text_content, chunk_size)

out = cv2.VideoWriter('output_video/encoded_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

frames = create_frames_from_chunks(binary_chunks, width, height)

for frame in frames:
    out.write(frame)

out.release()
