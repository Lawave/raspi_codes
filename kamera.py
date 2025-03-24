from picamera2 import Picamera2
from PIL import image
import io
from Flask import flask, response
import numpy as np
import threading

app = Flask(__name__)

picam2=Picamera2()
video_config = picam2.create_video_configuration(main={"size":(640,480)})
picam2.configure(video_config)
picam2.start()

def generate_frame():
    while True:
        frame = picam2.capture_array()
        image = Image.fromarray(frame).convert("RGB")
        stream = io.BytesIO()
        image.save(stream, format = 'JPEG')
        stream.seek(0)
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n')
        
@app.route('/')
def video_feed():
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace;boundary=frame')

if __name__ == '__main__':
    app.run(host='192.168.183.74', port=5005, threaded=True)