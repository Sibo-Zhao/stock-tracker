# app.py 内容
from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # 允许跨域请求

@app.route('/')
def home():
    return "Backend is running!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    