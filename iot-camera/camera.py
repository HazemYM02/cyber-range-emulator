from flask import Flask, Response
from PIL import Image, ImageDraw
import io, time, random

app = Flask(__name__)

@app.route('/')
def index():
    return 'OK - MJPEG at /stream'

@app.route('/stream')
def stream():
    def gen():
        while True:
            img = Image.new('RGB', (640, 360), (30, 30, 30))
            d = ImageDraw.Draw(img)
            ts = time.strftime('%Y-%m-%d %H:%M:%S')
            temp = round(random.uniform(20, 30), 2)
            d.text((10, 10), f"Camera 10.88.20.13\n{ts}\nTemp:{temp}C", fill=(255,255,255))
            buf = io.BytesIO()
            img.save(buf, format='JPEG', quality=70)
            frame = buf.getvalue()
            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
            time.sleep(0.2)
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
