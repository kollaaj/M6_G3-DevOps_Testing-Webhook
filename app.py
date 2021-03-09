from flask import Flask, render_template, request
from dotenv import load_dotenv
from datetime import datetime
import pymongo
import os

app = Flask(__name__)
load_dotenv()

mongo_uri = os.getenv('MONGO_URI')
mongo_client = pymongo.MongoClient(mongo_uri)

@app.route('/')
def index():
    triggers = list(mongo_client['hook']['triggers'].find({ 'action': { '$ne': 'started' } }).sort('_id', -1).limit(100))
    return render_template('index.html', triggers=triggers)

@app.route('/', methods=['POST'])
def webhook():
    trigger = request.get_json()
    trigger['my_timestamp'] = datetime.utcnow().strptime('%A %d %B %Y at %H:%M:%S')
    mongo_client['hook']['triggers'].insert_one(trigger)
    return ('', 204)
