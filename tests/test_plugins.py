import random
from plugin import Registry, register


@register
def say_hello(name):
    """Standard hello function"""
    return f"Hello {name}"

@register
def be_awesome(name):
    """Alternative awesome hello function"""
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(Registry().get_plugins()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
