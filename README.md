# TextStream

## Overview

TextStream is a project designed to encode textual data into a visual representation within a video file and decode it back to its original form. This project aims to demonstrate a method of embedding text data visually into a video stream using pixel blocks.

## Features

- **Text-to-Video Encoding**: Convert text data into a visual representation embedded in a video file.
- **Video-to-Text Decoding**: Extract text data from the encoded video back to its original form.
- **Visual Representation**: Binary data represented through pixel block patterns.

## Installation

### Requirements

- Python 
- OpenCV library 
- Numpy

### Setup Instructions

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.


### Encoding Text into Video

To encode text into a video:

1. Place the text in the `input/input_text` or replace txt doc with same directory.
2. Run the encoding script: `python encode.py`
3. you will find encoded video in `output/decoded_video.mp4`  directory.

### Decoding Video to Text

To decode a video back to text:

1. Place the video file in the `input_video/encoded_video.mp4` directory, replace with same name or change in code.
2. Run the decoding script: `python decode.py input_video.mp4`

## Example

Provide a brief example demonstrating the encoding and decoding process using a sample text file and video.
<img width="845" alt="Screenshot 2023-11-19 at 1 53 06 PM" src="https://github.com/scopophobic/TextStream/assets/66241061/5f1073d6-c028-4fa3-ba96-aff3148547d1">


## File Structure

- input/input_text.txt
- input_video/encoded_video.mp4
- output/decoded_text.txt
- encode.py
- decode.py
- README.md

## Credits

Acknowledge any external libraries, resources, or inspirations used in the project.

## Contributing

Specify guidelines for contributors and how they can contribute to the project.

## License

This project is licensed under the [MIT License](link-to-license).

