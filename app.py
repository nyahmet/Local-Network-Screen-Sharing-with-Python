from flask import Flask, render_template, Response
import cv2
import numpy as np
from PIL import ImageGrab
import socket
import threading
import tkinter as tk


app = Flask(__name__)


def gen_frames():
    while True:
        if app.is_streaming:
            img = ImageGrab.grab()
            frame = np.array(img)
            frame = cv2.resize(frame, (1920, 1080))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            ret, buffer = cv2.imencode('.png', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            img = np.zeros((480, 640, 3), dtype=np.uint8)
            img.fill(255)
            cv2.putText(img, 'Paused', (220, 240),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            ret, buffer = cv2.imencode('.jpg', img)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def start_stream():
    app.is_streaming = True

def stop_stream():
    app.is_streaming = False


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip_address = str(s.getsockname()[0]) + ":5000"
    except Exception:
        ip_address = 'Unable to determine IP address'
    finally:
        s.close()
    return ip_address




def create_gui():

    window = tk.Tk()
    window.title("Screen Sharing")


    start_button = tk.Button(window, text="Start", command=start_stream)
    start_button.pack()


    stop_button = tk.Button(window, text="Stop", command=stop_stream)
    stop_button.pack()


    ip_label = tk.Label(window, text="Address: " + get_ip_address())
    ip_label.pack()
    

    threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5000, 'debug': False}, daemon=True).start()
    
    app.is_streaming = False

    window.mainloop()


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    create_gui()





