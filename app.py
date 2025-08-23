from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return f"Hello World! Server IP: {ip_address}"

@app.route('/greet/<name>')
def greet_person(name):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return f"Hello, {name}! Server IP: {ip_address}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
