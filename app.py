from fastapi import FastAPI, WebSocket
import cv2
import numpy as np
from starlette.responses import StreamingResponse

app = FastAPI()

# Initialize the camera
camera = cv2.VideoCapture(0, cv2.CAP_V4L2)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        # Resize frame for faster processing (optional)
        frame = cv2.resize(frame, (640, 480))

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