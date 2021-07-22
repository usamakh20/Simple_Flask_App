from flask import Flask
import socket

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hostname = "+socket.gethostname()+"<br> Roll no. = 19I-1236 <br> Name = Usama Khalid"


if __name__ == '__main__':
    app.run()
