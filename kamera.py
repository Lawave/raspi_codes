from picamera2 import Picamera2
from PIL import Image
import io
from flask import Flask, Response
import threading

def start_video_server(host, port):
    app = Flask(__name__)
    picam2=Picamera2()
    video_config = picam2.create_video_configuration(
        main={"size": (640, 480)},
        controls={"FrameDurationLimits": (50000, 50000)}  # 1e6 / 50000 = 20 FPS
    )
    picam2.configure(video_config)
    picam2.start()

    @app.route('/')
    def stream():
        def generate():
            while True:
                frame = picam2.capture_array()
                image = Image.fromarray(frame).convert("RGB")
                stream = io.BytesIO()
                image.save(stream, format='JPEG')
                stream.seek(0)
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' +
                       stream.read() + b'\r\n')
        return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')
    print("Başladı")
    app.run(host=host, port=port, threaded=True)
    print("başladı")

'''
app = Flask(__name__)
picam2=Picamera2()
video_config = picam2.create_video_configuration(
    main={"size": (640, 480)},
    controls={"FrameDurationLimits": (50000, 50000)}  # 1e6 / 50000 = 20 FPS
)
picam2.configure(video_config)
picam2.start()
host = "172.20.10.3"
port = "5005"
start_video_server(app, picam2,host,port)
DOKUNMA!!!S
'''