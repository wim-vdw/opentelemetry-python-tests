from random import randint
from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Counter:
    def __init__(self):
        self._count = 0

    @property
    def count(self) -> str:
        return str(self._count)

    def increment(self):
        value = randint(1, 5)
        self._count += value
        logger.info(f'Counter incremented by {value}, current count: {self._count}')


cnt = Counter()


@app.route('/counter')
def counter():
    cnt.increment()

    return cnt.count
