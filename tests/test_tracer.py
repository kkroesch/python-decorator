import sys, logging
from unittest import TestCase
from tracer import trace, log, slow_down, timer

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

class TestTrace(TestCase):

    @trace
    def test_trace(name, location="World"):
        """ Nothing important here, but you can
            print(f"Hello {name} in {location}!")
        """
        pass

    @log
    def test_call_log_decorator(self):
        pass

    def test_param_and_result(self):        
        @trace
        def sum(a, b):
            return a + b
        self.assertEquals(4, sum(3, 1))

    def test_slow_down(self):
        @slow_down(rate=0.5)
        def countdown():
            for i in range(10,0):
                print(i)
        countdown()
    
    def test_timer(self):
        @timer
        def countdown():
            for i in range(10,0):
                print(i)
        countdown()
