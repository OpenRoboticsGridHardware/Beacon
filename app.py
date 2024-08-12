from fastapi import FastAPI
import cv2
import numpy as np
from starlette.responses import StreamingResponse
import os

app = FastAPI()

# Get resolution from environment variables or set default values
WIDTH = int(os.getenv("CAMERA_WIDTH", 640))
HEIGHT = int(os.getenv("CAMERA_HEIGHT", 480))

# Initialize the camera with the desired resolution
camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        # Encode frame to JPEG
        ret, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 75])
        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        # Yield frame bytes
        yield frame_bytes

@app.get("/video_feed")
def video_feed():
    def frame_generator():
        for frame_bytes in generate_frames():
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    return StreamingResponse(frame_generator(), media_type='multipart/x-mixed-replace; boundary=frame')

# For dynamic environment updates, consider restarting the server or use a method to reload configuration.
