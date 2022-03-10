from crypt import methods

from flask import Flask
from flask import request
from flask_cors import CORS
from Mapapi.parsejson import parsejson

from Mapapi.process import process

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        loc = request.json

    place_result = process(loc)
    json_data= parsejson(place_result)
    return json_data


 

    
