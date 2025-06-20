from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello! This Flask app is running on IPv4!'

if __name__ == '__main__':
    # Bind to all IPv4 addresses (0.0.0.0), port 5000
       serve(app, host='0.0.0.0', port=8000)