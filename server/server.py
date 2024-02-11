import flask
from flask import (
    Flask,
    jsonify,
    request
)
import json
import random
from backend import (
    get_search_response_from_zillow,
    display_search_items,
    get_zpid_api_response,
    display_zpid_info)


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

    
    api_response = get_search_response_from_zillow(
        location=parsed_data['location'],
        price_min=parsed_data['priceMin'],
        price_max=parsed_data['priceMax'],
        beds_min=parsed_data['bedsMin'],
        beds_max=parsed_data['bedsMax'],
        baths_min=parsed_data['bathsMin'],
        baths_max=parsed_data['bathsMax'],
        square_feet_min=parsed_data['sqftMin'],
        square_feet_max=parsed_data['sqftMax'],
        isApartment=parsed_data['isApartment'],
        isCondo=parsed_data['isCondo'],
        isTownhouse=parsed_data['isTownhouse'],
        sale_or_rent=parsed_data['saleOrRent']
    )
    
    dict_response = display_search_items(api_response)
    
    return jsonify(dict_response)
    
    
@app.route('/zpid', methods=['POST', 'GET'])
def get_zpid_info():
    data = request.get_data()
    parsed_data = json.loads(data)
    
    api_response = get_zpid_api_response(
        zpid=parsed_data['zpid']
    )
    
    dict_response = display_zpid_info(api_response)
    
    return jsonify(dict_response)

if __name__ == '__main__':
    app.run(debug=True)