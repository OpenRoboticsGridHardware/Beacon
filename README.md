# Raspberry Pi RGB LED Controller and Webcam Streamer

This project combines two functionalities:

1. **RGB LED Controller**: Manage RGB LEDs connected to a Raspberry Pi via a WebSocket server.
2. **Webcam Streamer**: Stream video from the Raspberry Pi's camera using Flask and OpenCV.

## Features

- **RGB LED Control**: Adjust the color of multiple RGB LEDs using PWM through a WebSocket server.
- **Webcam Streaming**: Broadcast the video feed from a connected camera over HTTP.

## Hardware Setup

### RGB LEDs

- **LED1**: GPIO 17 (Red), 27 (Green), 22 (Blue)
- **LED2**: GPIO 23 (Red), 24 (Green), 25 (Blue)
- **LED3**: GPIO 5 (Red), 6 (Green), 13 (Blue)

Ensure that your LEDs are correctly wired to these GPIO pins on your Raspberry Pi.

## Software Setup

### Prerequisites

Before you begin, make sure you have the following installed on your Raspberry Pi:

- **Raspberry Pi OS** (or another compatible Linux distribution)
- **Docker** and **Docker Compose**

### Installation Steps

1. **Install Docker and Docker Compose:**

    ```bash
    # Update package list
    sudo apt-get update

    # Install Docker
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh

    # Add your user to the docker group (optional but recommended)
    sudo usermod -aG docker $USER

    # Install Docker Compose
    sudo apt-get install docker-compose
    ```

2. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-repo/rgb-led-webcam.git
    cd rgb-led-webcam
    ```

3. **Build the Docker Image:**

    ```bash
    docker-compose build
    ```

4. **Run the Services with Docker Compose:**

    ```bash
    docker-compose up -d
    ```

### Docker Execution

If you prefer to run the Docker container directly without Docker Compose, you can use:

```bash
docker run -d --restart unless-stopped --privileged -p 5000:5000 -p 8765:8765 rgb-led-webcam
