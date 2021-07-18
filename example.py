
from tracer import slow_down, debug

import sys, logging
from unittest import TestCase
from tracer import trace, timer, log

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


@timer
@trace
def sum(a, b):
    return a + b

sum(1, 5)

@log
def did_something_with_meaningful_name():
    pass

did_something_with_meaningful_name()
