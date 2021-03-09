from flask import Flask, render_template, request
from dotenv import load_dotenv
import pymongo
import json
import os

app = Flask(__name__)
load_dotenv()

mongo_uri = os.getenv('MONGO_URI')
mongo_client = pymongo.MongoClient(mongo_uri)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    mongo_client['hook']['triggers'].insert_one(data)
    return ('', 204)
