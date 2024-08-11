from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['vr_tour_guide']
locations_collection = db['locations']

@app.route('/locations', methods=['POST'])
def add_location():
    location = request.json
    locations_collection.insert_one(location)
    return jsonify({'msg': 'Location added'}), 201

@app.route('/locations', methods=['GET'])
def get_locations():
    locations = list(locations_collection.find({}, {'_id': 0}))
    return jsonify(locations)

if __name__ == '__main__':
    app.run(debug=True)
