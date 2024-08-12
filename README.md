# Raspberry Pi RGB LED Controller and Webcam Streamer

This project combines two functionalities:

1. **RGB LED Controller:** Manage RGB LEDs connected to a Raspberry Pi via a WebSocket server.
2. **Webcam Streamer:** Stream video from the Raspberry Pi's camera using Flask and OpenCV.

## Features

- **RGB LED Control:** Adjust the color of multiple RGB LEDs using PWM through a WebSocket server.
- **Webcam Streaming:** Broadcast the video feed from a connected camera over HTTP.

## Hardware Setup

### RGB LEDs

Ensure that your LEDs are correctly wired to the following GPIO pins on your Raspberry Pi:

- **LED1:** 
  - Red: GPIO 17
  - Green: GPIO 27
  - Blue: GPIO 22

- **LED2:** 
  - Red: GPIO 23
  - Green: GPIO 24
  - Blue: GPIO 25

- **LED3:** 
  - Red: GPIO 5
  - Green: GPIO 6
  - Blue: GPIO 13

## Software Setup

### Prerequisites

Before you begin, ensure that the following software is installed on your Raspberry Pi:

- Raspberry Pi OS (or another compatible Linux distribution)
- Docker
- Docker Compose

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
    gh repo clone OpenRoboticsGridHardware/Beacon
    cd Beacon
    ```

3. **Build the Docker Image:**

    ```bash
    docker build -t beacon .
    ```

    - The `-t beacon` flag tags the image with the name `beacon`.

4. **Run the Services with Docker Compose:**

    ```bash
    docker-compose up -d
    ```

    - This will start the services defined in your `docker-compose.yml` file.

### Alternative Docker Execution

If you prefer to run the Docker container directly without Docker Compose, use the following command:

```bash
docker run -d --restart unless-stopped --privileged -p 5000:5000 -p 8765:8765 beacon
