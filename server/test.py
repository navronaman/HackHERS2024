import requests

# Define the URL of the Flask app
url = 'http://localhost:5000'

# Test the /generate_random_number endpoint
def test_generate_random_number():
    # Define the payload
    payload = {'min_threshold': 10, 'max_threshold': 100}
    
    # Send a POST request
    response = requests.post(f'{url}/generate_random_number', json=payload)
        
    # Parse the JSON response
    data = response.json()
    # Print the random number
    print(data)

# Run the test
test_generate_random_number()
