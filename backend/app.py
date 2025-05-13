from flask import Flask, Response
from flask_cors import CORS
from flask_socketio import SocketIO
import cv2
import torch

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best.pt')
model.conf = 0.6  # confidence threshold

# Video stream function
def generate():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        results = model(frame)
        annotated_frame = results.render()[0]
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def home():
    return "Fluent Fingers Backend Running"

@app.route('/video')
def video():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
