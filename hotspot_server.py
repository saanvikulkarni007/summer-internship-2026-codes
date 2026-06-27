from flask import Flask, send_file, render_template_string
import cv2
import socket
import os

app = Flask(__name__)

PHOTO_PATH = "captured_photo.jpg"

def capture_photo():
    """Capture photo from front (default) camera"""
    cam = cv2.VideoCapture(0)  # 0 = front/default camera
    if not cam.isOpened():
        print("Camera not accessible!")
        return False
    ret, frame = cam.read()
    if ret:
        cv2.imwrite(PHOTO_PATH, frame)
        print("Photo captured!")
    cam.release()
    return ret

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello from Hotspot!</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background: #1a1a2e;
            color: white;
            padding: 40px;
        }
        h1 { color: #e94560; font-size: 2.5em; }
        img {
            border-radius: 20px;
            border: 4px solid #e94560;
            max-width: 90%;
            margin-top: 20px;
        }
        p { font-size: 1.2em; color: #a8a8b3; }
    </style>
</head>
<body>
    <h1>👋 Hello, Saanvi!</h1>
    <p>You connected from: <b>{{ ip }}</b></p>
    <p>Here's a photo from the server's front camera:</p>
    <img src="/photo" alt="Server Camera Photo" />
</body>
</html>
"""

@app.route("/")
def index():
    from flask import request
    client_ip = request.remote_addr

    # Try to get hostname from IP
    try:
        device_name = socket.gethostbyaddr(client_ip)[0]
    except:
        device_name = client_ip  # fallback to IP if name not found

    # Capture fresh photo every visit
    capture_photo()

    return render_template_string(HTML_TEMPLATE, device_name=device_name, ip=client_ip)

@app.route("/photo")
def photo():
    if os.path.exists(PHOTO_PATH):
        return send_file(PHOTO_PATH, mimetype="image/jpeg")
    return "No photo available", 404

if __name__ == "__main__":
    print("Server starting on http://0.0.0.0:5000")
    print("Connect your phone to the hotspot, then open: http://192.168.137.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)