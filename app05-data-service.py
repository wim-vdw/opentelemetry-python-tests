from flask import Flask
import requests

app = Flask(__name__)


@app.route('/data')
def data() -> dict:
    """
    Endpoint to get a random city and car brand.

    Returns:
        dict: A dictionary with a random city and car brand.
    """
    response = requests.get('http://localhost:8081/city')
    city = response.json()['city']
    response = requests.get('http://localhost:8082/car')
    car = response.json()['car']
    return {
        'city': city,
        'car': car,
    }
