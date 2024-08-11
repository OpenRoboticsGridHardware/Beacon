# Raspberry Pi RGB LED Controller and Webcam Streamer

This project combines two functionalities:

1. **RGB LED Controller**: Control RGB LEDs connected to a Raspberry Pi via a WebSocket server.
2. **Webcam Streamer**: Stream video from the Raspberry Pi's camera using Flask and OpenCV.

## Features

- **RGB LED Control**: Control the color of multiple RGB LEDs using PWM via a WebSocket server.
- **Webcam Streaming**: Stream the video feed from a connected camera over HTTP.

## Hardware Setup

- **LED1**: Connected to GPIO 17 (Red), 27 (Green), 22 (Blue).
- **LED2**: Connected to GPIO 23 (Red), 24 (Green), 25 (Blue).
- **LED3**: Connected to GPIO 5 (Red), 6 (Green), 13 (Blue).

## Software Setup

### Prerequisites

Ensure your Raspberry Pi has the following installed:

- Raspberry Pi OS (or another compatible Linux distribution).
- Docker and Docker Compose.

### Installation

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

Alternatively, you can use Docker to run both services:

```bash
docker run -d --restart unless-stopped --privileged -p 5000:5000 -p 8765:8765 rgb-led-webcam

#### Docker Compose Configuration

The `docker-compose.yml` file defines the services and their configurations. It includes the `privileged` mode to allow access to GPIO pins:

```yaml
version: '3.7'

services:
  rgb-led-webcam:
    image: rgb-led-webcam
    build: .
    ports:
      - "5000:5000"
      - "8765:8765"
    restart: unless-stopped
    privileged: true



