from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "SecOps-GitForge Pipeline Running Securely!"

if __name__ == '__main__':
    host = os.getenv('HOST', '127.0.0.1')
    app.run(host=host, port=5000)
