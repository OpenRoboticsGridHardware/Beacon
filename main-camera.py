import cv2
import time
from flask import Flask, Response, stream_with_context

app = Flask(__name__)

def get_max_resolution(camera):
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)  
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000) 
    max_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    max_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    return max_width, max_height

def generate_frames():
    camera = cv2.VideoCapture(0, cv2.CAP_V4L2) 
    if not camera.isOpened():
        print("Error: Could not open camera.")
        return
    
    max_width, max_height = get_max_resolution(camera)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, max_width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, max_height)
    
    print(f"Camera set to maximum resolution: {max_width}x{max_height}")

    while True:
        success, frame = camera.read()
        if not success:
            print("Error: Could not read frame from camera.")
            break
        ret, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
        if not ret:
            print("Error: Could not encode frame.")
            break

        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    camera.release()

@app.route('/video_feed')
def video_feed():
    return Response(stream_with_context(generate_frames()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False, use_reloader=False)
