import flask
from flask import (
    Flask,
    jsonify,
    request
)
import json
import random

app = Flask(__name__)

# Some API route
@app.route('/hello')
def hello():
    return jsonify({
        'message': 'Hello World!',
        'random': f'{random.randint(0, 1000)}'})

@app.route('/generate_random_number', methods=['POST'])
def generate_random_number():
    # Get threshold values from request
    min_threshold = int(request.json['min_threshold'])
    max_threshold = int(request.json['max_threshold'])
    
    # Generate random number within the specified range
    random_num = random.randint(min_threshold, max_threshold)
    
    # Return JSON response with the random number
    return jsonify({'random_number': random_num})


@app.route('/search', methods=['POST', 'GET'])
def get_property_info():
    data = request.get_data()
    parsed_data = json.loads(data)
    location = parsed_data['location']
    price = parsed_data['price']
    
    return jsonify({'zestimate': 4000, 'price': 16888, 'images': ['https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png']})
    
    

if __name__ == '__main__':
    app.run(debug=True)