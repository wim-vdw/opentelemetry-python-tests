from flask import Flask
from random import choice, randint
from time import sleep

app = Flask(__name__)


@app.route('/car')
def car() -> dict:
    """
    Endpoint to get a random car brand.

    Returns:
        dict: A dictionary with a random car brand.

    Note:
        This function simulates a delay by sleeping for a random duration between 1 and 200 milliseconds.
    """
    cars = ['BMW', 'Ferrari', 'Porsche', 'Audi', 'Mercedes', 'Lamborghini', 'Koenigsegg', 'Bugatti', 'McLaren']
    sleep(randint(1, 200) / 1000)

    return {'car': choice(cars)}
