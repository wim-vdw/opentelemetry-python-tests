from flask import Flask
from random import choice, randint
from time import sleep

app = Flask(__name__)


@app.route('/city')
def city() -> dict:
    """
    Endpoint to get a random city name.

    Returns:
        dict: A dictionary with a random city name.

    Note:
        This function simulates a delay by sleeping for a random duration between 1 and 200 milliseconds.
    """
    cities = ['Antwerp', 'Berlin', 'Rome', 'London', 'Paris', 'New York', 'Tokyo']
    sleep(randint(1, 200) / 1000)

    return {'city': choice(cities)}
