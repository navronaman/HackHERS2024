import flask
from flask import (
    Flask,
    jsonify,
    request
)
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


if __name__ == '__main__':
    app.run(debug=True)