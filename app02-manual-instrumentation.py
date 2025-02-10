from random import randint
from flask import Flask
from opentelemetry import trace, metrics
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Acquire a tracer.
tracer = trace.get_tracer('counter.tracer')

# Acquire a meter.
meter = metrics.get_meter('counter.meter')

# Create a counter.
increase_counter = meter.create_counter(
    'increase.counts',
    description='The number of increases by increase value',
)


class Counter:
    def __init__(self):
        self._count = 0

    @property
    def count(self) -> str:
        return str(self._count)

    def increment(self):
        with tracer.start_as_current_span('counter') as counter_span:
            increase = randint(1, 5)
            self._count += increase
            counter_span.set_attribute('counter.increase', increase)
            counter_span.set_attribute('counter.value', self._count)
            increase_counter.add(1, {'counter.increase': increase})


cnt = Counter()


@app.route('/counter')
def counter():
    cnt.increment()

    return cnt.count
