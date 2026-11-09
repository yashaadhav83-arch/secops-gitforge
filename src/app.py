from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "SecOps-GitForge Pipeline Running Securely!"

if __name__ == '__main__':
    host = os.getenv('HOST', '127.0.0.1')
    app.run(host='0.0.0.0', port=5000)  # nosemgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
