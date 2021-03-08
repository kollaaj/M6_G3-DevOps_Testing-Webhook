from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    data_str = json.dumps(data)
    print(data_str)
    return ('', 204)
