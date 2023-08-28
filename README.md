# Screen Sharing App using Flask and OpenCV

This is a simple screen sharing application built using Flask, OpenCV, and tkinter. The app allows you to stream your screen's content to a web browser using a local server. Users can start and stop the streaming, and the app provides the IP address for accessing the stream in a browser.

## Requirements

- Python 3.x
- Flask
- OpenCV (`cv2`)
- NumPy
- Pillow (`PIL`)
- tkinter
- Socket

## Installation

1. Clone or download the repository to your local machine.
2. Make sure you have all the required packages installed. You can use the following command to install them:

   ```bash
   pip install Flask opencv-python numpy Pillow

## Usage

1. Run the 'app.py' script using the following command:
   
   ```bash
   python app.py

2. A GUI window will appear with "Start" and "Stop" buttons for controlling the screen sharing. It will also display the IP address and port that you can use to access the stream in your browser.
3. Click the "Start" button to begin streaming your screen content. The screen content will be visible in your browser at the provided IP address.
4. Click the "Stop" button to stop the streaming.

## Code Overview

### 'app.py'

- Imports necessary libraries: Flask, cv2, numpy, ImageGrab, socket, threading, and tkinter.
- Initializes a Flask app.
- Defines a function 'gen_frames()' to continuously capture the screen content, convert it to frames, and encode them into PNG images to be streamed.
- Defines functions 'start_stream()' and stop_stream() to control the streaming.
- Defines a function 'get_ip_address()' to determine the local IP address.
- Defines a function 'create_gui()' to create the tkinter GUI with "Start" and "Stop" buttons and IP address display.
- Defines routes using Flask decorators:
 * '/video_feed' route streams frames in a multipart format.
 * '/ route renders' an HTML template (not included in the code snippet).
- Launches the Flask app using a new thread, starts with streaming set to 'False'.
- Calls 'create_gui()' to start the GUI.


## Disclaimer

This code is provided as-is for educational purposes and may not be suitable for production use. Use at your own risk.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

ahmetnuri.yilmaz@hotmail.com

