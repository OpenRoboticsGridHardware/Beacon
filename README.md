# Raspberry Pi RGB LED Controller and Webcam Streamer

This project combines two functionalities:

1. **RGB LED Controller**: Control RGB LEDs connected to a Raspberry Pi via a WebSocket server.
2. **Webcam Streamer**: Stream video from the Raspberry Pi's camera using Flask and OpenCV.

## Features

- **RGB LED Control**: Control the color of multiple RGB LEDs using PWM via a WebSocket server.
- **Webcam Streaming**: Stream the video feed from a connected camera over HTTP.

## Requirements

- Raspberry Pi with Raspbian OS.
- Python 3.
- RGB LEDs connected to GPIO pins.
- A camera compatible with OpenCV (e.g., Raspberry Pi Camera Module).

## Hardware Setup

- **LED1**: Connected to GPIO 17 (Red), 27 (Green), 22 (Blue).
- **LED2**: Connected to GPIO 23 (Red), 24 (Green), 25 (Blue).
- **LED3**: Connected to GPIO 5 (Red), 6 (Green), 13 (Blue).

## Software Setup

### Prerequisites

Install the following dependencies:

- `libgl1-mesa-glx`
- `libglib2.0-0`
- `libsm6`
- `libxext6`
- `libxrender-dev`
- `python3`
- `python3-pip`
- `opencv-python`
- `flask`
- `websockets`
- `RPi.GPIO`

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-repo/rgb-led-webcam.git
    cd rgb-led-webcam
    ```

2. Install the required Python packages:
    ```bash
    pip3 install -r requirements.txt
    ```

3. Build the Docker image:
    ```bash
    docker build -t rgb-led-webcam .
    ```

### Running the Application

You can run the application either directly on the Raspberry Pi or within a Docker container.

#### Direct Execution

1. Start the Flask app for webcam streaming:
    ```bash
    python3 flask_app.py
    ```

2. Start the WebSocket server for LED control:
    ```bash
    python3 websocket_server.py
    ```

#### Docker Execution

Alternatively, you can use Docker to run both services:

```bash
docker run -p 5000:5000 -p 8765:8765 rgb-led-webcam
