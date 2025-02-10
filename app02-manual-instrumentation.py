from random import randint
from flask import Flask
from opentelemetry import trace
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Acquire a tracer
tracer = trace.get_tracer("counter.tracer")


class Counter:
    def __init__(self):
        self._count = 0

    @property
    def count(self) -> str:
        return str(self._count)

    def increment(self):
        with tracer.start_as_current_span('counter') as span:
            value = randint(1, 5)
            self._count += value
            span.set_attribute('counter.increase', value)
            span.set_attribute('counter.value', self._count)


cnt = Counter()


@app.route('/counter')
def counter():
    cnt.increment()

    return cnt.count
